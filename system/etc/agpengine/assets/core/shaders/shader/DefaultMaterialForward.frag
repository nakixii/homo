#version 460 core
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

// includes

#include "core/shaders/common/core_default_camera_structures_common.h"
#include "core/shaders/common/post_process_common.h"
#include "core/shaders/common/tonemap_common.h"

#include "common/default_material_env_structures_common.h"
#include "common/default_light_structures_common.h"
#include "common/default_material_structures_common.h"

#include "common/brdf_common.h"
#include "common/lighting_common.h"
#include "common/shadowing_common.h"

#define CORE_GEOMETRIC_SPECULAR_AA_ROUGHNESS 0
#define CORE_PBR_FRAG_EPSILON 0.0001

#define CORE_ENABLE_POINT_SPOT_LIGHTS 0

// sets

layout(set = 0, binding = 0, std140) uniform uCameraMatrices
{
    DefaultCameraMatrixStruct uCameras[CORE_MAX_DEFAULT_CAMERA_COUNT];
};

layout(set = 1, binding = 0, std140) uniform uEnvironmentData
{
    DefaultMaterialEnvironmentStruct uEnvironment;
};
layout(set = 1, binding = 1, std140) uniform uLightData
{
    DefaultMaterialLightStruct uLights[CORE_MAX_DEFAULT_LIGHT_COUNT];
};
layout(set = 1, binding = 2, std140) uniform uLightCountData
{
    DefaultMaterialLightCountStruct uLightCounts;
};
layout(set = 1, binding = 3) uniform texture2D uTexDirShadow;
layout(set = 1, binding = 4) uniform texture2D uTexSpotShadow;
layout(set = 1, binding = 5) uniform textureCube uTexRadiance;
layout(set = 1, binding = 6) uniform sampler uSamplerShadow;
layout(set = 1, binding = 7) uniform sampler uSamplerCube;

layout(set = 3, binding = 0) uniform CORE_RELAXEDP texture2D uTexBaseColor;
layout(set = 3, binding = 1) uniform CORE_RELAXEDP texture2D uTexNormal;
layout(set = 3, binding = 2) uniform CORE_RELAXEDP texture2D uTexMaterial;
layout(set = 3, binding = 3) uniform CORE_RELAXEDP texture2D uTexEmissive;
layout(set = 3, binding = 4) uniform CORE_RELAXEDP texture2D uTexAo;
layout(set = 3, binding = 5) uniform sampler uSampler;

layout(push_constant, std430) uniform uPushConstant
{
    DefaultMaterialPushConstantStruct uObjectPushConstant;
};

layout(constant_id = 0) const uint CORE_MATERIAL_TYPE = 0;
layout(constant_id = 1) const uint CORE_MATERIAL_FLAGS = 0;
layout(constant_id = 2) const uint CORE_LIGHTING_FLAGS = 0;
layout(constant_id = 3) const uint CORE_POST_PROCESS_FLAGS = 0;

// in / out

layout(location = 0) in vec3 inPos;       // viewspace
layout(location = 1) in CORE_RELAXEDP vec3 inNormal;    // viewspace
layout(location = 2) in CORE_RELAXEDP vec4 inTangentW;  // viewspace
layout(location = 3) in vec4 inShadowCoord;
layout(location = 4) in vec2 inUv;
layout(location = 5) in CORE_RELAXEDP vec4 inColor;

layout (location = 0) out vec4 outColor;

//

struct ShadingVectors {
    vec3 N;
    float NoV;
    vec3 L;
    float NoL;
    vec3 V;
    vec3 faceNormal;
};

struct ClearCoatShadingVariables {
    float alpha2;
    float clearCoat;
};

vec3 getIrradianceSample(
    const vec3 worldNormal)
{
    return unpackIblIrradianceSH(worldNormal, uEnvironment.shIndirectCoefficients)
        * uEnvironment.indirectDiffuseColorFactor.rgb;
}

vec3 getRadianceSample(
    const vec3 worldReflect,
    const float roughness)
{
    const CORE_RELAXEDP float cubeLod = uEnvironment.indirectSpecularColorFactor.a * roughness;
    const vec3 worldReflectEnv = mat3(uEnvironment.envRotation) * worldReflect;
    return unpackIblRadiance(CORE_TEXTURE_LOD_CUBE(samplerCube(uTexRadiance, uSamplerCube),
        worldReflectEnv, cubeLod)) * uEnvironment.indirectSpecularColorFactor.rgb;
}

mat4 getShadowMatrix(const uint shadowCamIdx)
{
    return uCameras[shadowCamIdx].shadowViewProj;
}

vec3 calcDirectionalLight(
    uint currLightIdx,
    vec3 materialDiffuseBRDF,
    vec3 f0,
    float alpha2,
    ShadingVectors sv,
    ClearCoatShadingVariables ccsv)
{
    const vec3 H = normalize(sv.L + sv.V);
    const float VoH = clamp(dot(sv.V, H), 0.0, 1.0);
    const float NoH = clamp(dot(sv.N, H), 0.0, 1.0);

    float attenuationCC = 1.0;
    vec3 calculatedColor = vec3(0.0);
    if ((CORE_MATERIAL_FLAGS & CORE_MATERIAL_CLEAR_COAT_BIT)
        == CORE_MATERIAL_CLEAR_COAT_BIT) {
        const float NoLCC = clamp(dot(sv.faceNormal, sv.L), CORE_PBR_FRAG_EPSILON, 1.0);
        const float NoHCC = clamp(dot(sv.faceNormal, H), 0.0, 1.0);
        const float f0CC = 0.04;

        const float D = dGGX(ccsv.alpha2, NoHCC);
        const float G = vKelemen(NoHCC);
        const float F = fSchlickSingle(f0CC, VoH) * ccsv.clearCoat;
        const float specClearCoat = F * D * G;

        attenuationCC = 1.0 - F;
        calculatedColor += vec3(specClearCoat * NoLCC);
    }
    const float D = dGGX(alpha2, NoH);
    const float G = vGGXWithCombinedDenominator(alpha2, sv.NoV, sv.NoL);
    const vec3 F = fSchlick(f0, VoH);
    const vec3 specContrib = F * (D * G);

    const vec3 diffuseContrib = (1.0 - F) * materialDiffuseBRDF;
    calculatedColor += (diffuseContrib + specContrib * attenuationCC) * attenuationCC * sv.NoL;

    const vec3 lightColor = uLights[currLightIdx].color.xyz;
    return calculatedColor * lightColor;
}

#define CORE_USE_CLEAR_COAT_WITH_POINTS 0

vec3 calcPointLight(
    uint currLightIdx,
    vec3 pointToLight,
    float dist,
    vec3 materialDiffuseBRDF,
    vec3 f0,
    float alpha2,
    ShadingVectors sv,
    ClearCoatShadingVariables ccsv)
{
    const float range = uLights[currLightIdx].dir.w;
    const float attenuation = max(min(1.0 - pow(dist / range, 4.0), 1.0), 0.0)
        / (dist * dist);

    const vec3 H = normalize(sv.L + sv.V);
    const float VoH = clamp(dot(sv.V, H), 0.0, 1.0);
    const float NoH = clamp(dot(sv.N, H), 0.0, 1.0);

    float attenuationCC = 1.0;
    vec3 calculatedColor = vec3(0.0);
#if (CORE_USE_CLEAR_COAT_WITH_POINTS == 1)
    if ((CORE_MATERIAL_FLAGS & CORE_MATERIAL_CLEAR_COAT_BIT)
        == CORE_MATERIAL_CLEAR_COAT_BIT) {
        const float NoLCC = clamp(dot(sv.faceNormal, sv.L), CORE_PBR_FRAG_EPSILON, 1.0);
        const float NoHCC = clamp(dot(sv.faceNormal, H), 0.0, 1.0);
        const float f0CC = 0.04;

        const float D = dGGX(ccsv.alpha2, NoHCC);
        const float G = vKelemen(NoHCC);
        const float F = fSchlickSingle(f0CC, VoH) * ccsv.clearCoat;
        const float specClearCoat = F * D * G;

        attenuationCC = 1.0 - F;
        calculatedColor += vec3(specClearCoat * NoLCC);
    }
#endif

    const float D = dGGX(alpha2, NoH);
    const float G = vGGXWithCombinedDenominator(alpha2, sv.NoV, sv.NoL);
    const vec3 F = fSchlick(f0, VoH);
    const vec3 specContrib = F * (D * G);

    const vec3 diffuseContrib = (1.0 - F) * materialDiffuseBRDF;
    calculatedColor += (diffuseContrib + specContrib * attenuationCC) * attenuationCC * sv.NoL;

    const vec3 lightColor = uLights[currLightIdx].color.xyz;
    return calculatedColor * lightColor * attenuation;
}

vec3 calcLighting(
    vec3 diffuseColor,
    vec3 f0,
    float alpha2,
    ShadingVectors sv,
    ClearCoatShadingVariables ccsv)
{
    const vec3 materialDiffuseBRDF = diffuseColor * diffuseCoeff();
    vec3 color = vec3(0.0);
    const uint directionalLightCount = uLightCounts.directionalLightCount;
    const uint directionalLightBeginIndex = uLightCounts.directionalLightBeginIndex;
    for (uint lightIdx = 0; lightIdx < directionalLightCount; ++lightIdx) {
        const uint currLightIdx = directionalLightBeginIndex + lightIdx;
        sv.L = -uLights[currLightIdx].dir.xyz; // normalization already done in c-code
        sv.NoL = clamp(dot(sv.N, sv.L), 0.0, 1.0);

        CORE_RELAXEDP float shadowCoeff = 1.0;
        if ((CORE_MATERIAL_FLAGS & CORE_MATERIAL_SHADOW_RECEIVER_BIT)
            == CORE_MATERIAL_SHADOW_RECEIVER_BIT) {
            const uint lightFlags = uLights[currLightIdx].flags.x;
            if ((lightFlags & CORE_LIGHT_USAGE_SHADOW_LIGHT_BIT) == CORE_LIGHT_USAGE_SHADOW_LIGHT_BIT) {
                if ((CORE_LIGHTING_FLAGS & CORE_LIGHTING_SHADOW_TYPE_VSM_BIT) == CORE_LIGHTING_SHADOW_TYPE_VSM_BIT) {
                    shadowCoeff = calcVsmShadow(uTexDirShadow, uSampler, inShadowCoord, sv.NoL);
                } else {
                    shadowCoeff = calcPcfShadow(uTexDirShadow, uSamplerShadow, inShadowCoord, sv.NoL);
                }
            }
        }

        color += calcDirectionalLight(currLightIdx,
            materialDiffuseBRDF, f0, alpha2, sv, ccsv) * shadowCoeff;
    }

    if ((CORE_LIGHTING_FLAGS & CORE_LIGHTING_SPOT_ENABLED_BIT) == CORE_LIGHTING_SPOT_ENABLED_BIT) {
        const uint cameraIdx = uObjectPushConstant.indices.z;
        // world pos not currently coming from VS
        const vec3 worldPos = (uCameras[cameraIdx].viewInv * vec4(inPos.xyz, 1.0)).xyz;
        const uint spotLightCount = uLightCounts.spotLightCount;
        const uint spotLightLightBeginIndex = uLightCounts.spotLightBeginIndex;
        for (uint spotIdx = 0; spotIdx < spotLightCount; ++spotIdx) {
            const uint currLightIdx = spotLightLightBeginIndex + spotIdx;

            const vec3 pointToLight = uLights[currLightIdx].pos.xyz - inPos.xyz;
            const float dist = length(pointToLight);
            sv.L = pointToLight / dist;
            sv.NoL = clamp(dot(sv.N, sv.L), 0.0, 1.0);

            CORE_RELAXEDP float shadowCoeff = 1.0;
            if ((CORE_MATERIAL_FLAGS & CORE_MATERIAL_SHADOW_RECEIVER_BIT)
                == CORE_MATERIAL_SHADOW_RECEIVER_BIT) {
                const uvec2 lightFlags = uLights[currLightIdx].flags.xy;
                if ((lightFlags.x & CORE_LIGHT_USAGE_SHADOW_LIGHT_BIT) == CORE_LIGHT_USAGE_SHADOW_LIGHT_BIT) {
                    const vec4 spotShadowCoord = getShadowMatrix(lightFlags.y) * vec4(worldPos.xyz, 1.0);
                    if ((CORE_LIGHTING_FLAGS & CORE_LIGHTING_SHADOW_TYPE_VSM_BIT) == CORE_LIGHTING_SHADOW_TYPE_VSM_BIT) {
                        shadowCoeff = calcVsmShadow(uTexSpotShadow, uSampler, spotShadowCoord, sv.NoL);
                    } else {
                        shadowCoeff = calcPcfShadow(uTexSpotShadow, uSamplerShadow, spotShadowCoord, sv.NoL);
                    }
                }
            }

            const float lightAngleScale = uLights[currLightIdx].spotLightParams.x;
            const float lightAngleOffset = uLights[currLightIdx].spotLightParams.y;
            // See: https://github.com/KhronosGroup/glTF/tree/master/extensions/2.0/Khronos/KHR_lights_punctual
            const float cd = dot(uLights[currLightIdx].dir.xyz, -sv.L);
            const float angularAttenuation = clamp(cd * lightAngleScale + lightAngleOffset, 0.0, 1.0);

            color += calcPointLight(currLightIdx, pointToLight, dist,
                materialDiffuseBRDF, f0, alpha2, sv, ccsv) * (angularAttenuation * angularAttenuation) * shadowCoeff;
        }
    }
    if ((CORE_LIGHTING_FLAGS & CORE_LIGHTING_POINT_ENABLED_BIT) == CORE_LIGHTING_POINT_ENABLED_BIT) {
        const uint pointLightCount = uLightCounts.pointLightCount;
        const uint pointLightBeginIndex = uLightCounts.pointLightBeginIndex;
        for (uint pointIdx = 0; pointIdx < pointLightCount; ++pointIdx) {
            const uint currLightIdx = pointLightBeginIndex + pointIdx;

            const vec3 pointToLight = uLights[currLightIdx].pos.xyz - inPos.xyz;
            const float dist = length(pointToLight);
            sv.L = pointToLight / dist;
            sv.NoL = clamp(dot(sv.N, sv.L), 0.0, 1.0);

            color += calcPointLight(currLightIdx, pointToLight, dist,
                materialDiffuseBRDF, f0, alpha2, sv, ccsv);
        }
    }

    return color;
}

///////////////////////////////////////////////////////////////////////////////
// "main" functions

vec4 unlitBasic()
{
    const CORE_RELAXEDP vec4 baseColor = CORE_TEXTURE_2D(sampler2D(uTexBaseColor, uSampler), inUv)
        * uObjectPushConstant.baseColor * inColor;
    if ((CORE_MATERIAL_FLAGS & CORE_MATERIAL_ADDITIONAL_SHADER_DISCARD_BIT) ==
        CORE_MATERIAL_ADDITIONAL_SHADER_DISCARD_BIT) {
        if (baseColor.a < uObjectPushConstant.material3.a)
        {
            discard;
        }
    }
    return baseColor;
}

vec4 unlitShadowAlpha()
{
    const CORE_RELAXEDP vec4 baseColor = CORE_TEXTURE_2D(sampler2D(uTexBaseColor, uSampler), inUv)
        * uObjectPushConstant.baseColor * inColor;
    if ((CORE_MATERIAL_FLAGS & CORE_MATERIAL_ADDITIONAL_SHADER_DISCARD_BIT) ==
        CORE_MATERIAL_ADDITIONAL_SHADER_DISCARD_BIT) {
        if (baseColor.a < uObjectPushConstant.material3.a) {
            discard;
        }
    }
    const vec3 N = normalize(inNormal.xyz);

    const uint directionalLightCount = uLightCounts.directionalLightCount;
    const uint directionalLightBeginIndex = uLightCounts.directionalLightBeginIndex;
    CORE_RELAXEDP vec4 color = baseColor;
    for (uint lightIdx = 0; lightIdx < directionalLightCount; ++lightIdx) {
        const uint currLightIdx = directionalLightBeginIndex + lightIdx;
        const vec3 L = -uLights[currLightIdx].dir.xyz; // normalization already done in c-code
        const float NoL = clamp(dot(N, L), 0.0, 1.0);

        const uint lightFlags = uLights[currLightIdx].flags.x;
        CORE_RELAXEDP float shadowCoeff = 1.0;
        if ((CORE_MATERIAL_FLAGS & CORE_MATERIAL_SHADOW_RECEIVER_BIT)
            == CORE_MATERIAL_SHADOW_RECEIVER_BIT) {
            if ((CORE_LIGHTING_FLAGS & CORE_LIGHTING_SHADOW_TYPE_VSM_BIT) == CORE_LIGHTING_SHADOW_TYPE_VSM_BIT) {
                shadowCoeff = calcVsmShadow(uTexDirShadow, uSampler, inShadowCoord, NoL);
            } else {
                shadowCoeff = calcPcfShadow(uTexDirShadow, uSamplerShadow, inShadowCoord, NoL);
            }
        }

        color.rgba *= (1.0 - shadowCoeff);
    }

    return color;
}

vec4 pbrBasic()
{
    const CORE_RELAXEDP vec4 baseColor = CORE_TEXTURE_2D(sampler2D(uTexBaseColor, uSampler), inUv)
        * uObjectPushConstant.baseColor * inColor;
    if ((CORE_MATERIAL_FLAGS & CORE_MATERIAL_ADDITIONAL_SHADER_DISCARD_BIT) ==
        CORE_MATERIAL_ADDITIONAL_SHADER_DISCARD_BIT) {
        if (baseColor.a < uObjectPushConstant.material3.a) {
            discard;
        }
    }

    const vec3 normNormal = normalize(inNormal.xyz);
    vec3 N;
    if ((CORE_MATERIAL_FLAGS & CORE_MATERIAL_NORMAL_MAP_BIT)
        == CORE_MATERIAL_NORMAL_MAP_BIT) {
        vec3 normal = CORE_TEXTURE_2D(sampler2D(uTexNormal, uSampler), inUv).rgb;
        // glTF uses right handed normal maps. Must flip green (Y) to get left handed.
        normal.g = 1.0 - normal.g;
        const float normalScale = uObjectPushConstant.material3.x;
        normal = normalize((2.0 * normal - 1.0) * vec3(normalScale, normalScale, 1.0f));
        const vec3 tangent = normalize(inTangentW.xyz);
        const vec3 bitangent = cross(normNormal, tangent.xyz) * inTangentW.w;
        const mat3 tbn = mat3(
            tangent.xyz,
            bitangent.xyz,
            normNormal);
        N = normalize(tbn * normal);
    } else {
        N = normNormal;
    }

    if ((CORE_MATERIAL_FLAGS & CORE_MATERIAL_DOUBLE_SIDED_BIT)
        == CORE_MATERIAL_DOUBLE_SIDED_BIT) {
        N = gl_FrontFacing ? N : -N;
    }

    const CORE_RELAXEDP vec4 material = CORE_TEXTURE_2D(sampler2D(uTexMaterial, uSampler), inUv) * uObjectPushConstant.material;
    const CORE_RELAXEDP float ao = clamp(CORE_TEXTURE_2D(sampler2D(uTexAo, uSampler), inUv).x * uObjectPushConstant.material2.a, 0.0, 1.0);

    CORE_RELAXEDP float roughness;
    CORE_RELAXEDP vec3 f0;
    CORE_RELAXEDP vec3 diffuseColor;
    if (CORE_MATERIAL_TYPE == CORE_MATERAL_SPECULAR_GLOSSINESS) {
        f0 = material.xyz;
        diffuseColor = baseColor.rgb * (1.0 - max(f0.x, max(f0.y, f0.z)));
        roughness = 1.0 - clamp(material.a, 0.0, 1.0);
    } else {
        const CORE_RELAXEDP float metallic = clamp(material.b, 0.0, 1.0);
        f0 = mix(vec3(uObjectPushConstant.material.a), baseColor.rgb, metallic);
        diffuseColor = mix(baseColor.rgb * (1.0 - f0), vec3(0.0), vec3(metallic));
        roughness = material.g;
    }
#if(CORE_GEOMETRIC_SPECULAR_AA_ROUGHNESS == 1)
    // reduce shading aliasing by increasing roughness based on the curvature of the geometry
    const vec3 normalDFdx = dFdx(normNormal);
    const vec3 normalDdFdy = dFdy(normNormal);
    const float geometricRoughness =
        pow(clamp(max(dot(normalDFdx, normalDFdx), dot(normalDdFdy, normalDdFdy)), 0.0, 1.0), 0.333);
    roughness = max(roughness, geometricRoughness);
#endif
    roughness = clamp(roughness, CORE_BRDF_MIN_ROUGHNESS, 1.0);

    const CORE_RELAXEDP float alpha = roughness * roughness;
    const CORE_RELAXEDP float alpha2 = alpha * alpha;

    const vec3 V = -normalize(inPos);
    const float NoV = clamp(dot(N, V), CORE_PBR_FRAG_EPSILON, 1.0);

    CORE_RELAXEDP float roughnessCC;
    CORE_RELAXEDP float alpha2CC;
    CORE_RELAXEDP float clearCoat;
    if ((CORE_MATERIAL_FLAGS & CORE_MATERIAL_CLEAR_COAT_BIT)
        == CORE_MATERIAL_CLEAR_COAT_BIT) {
        roughnessCC = uObjectPushConstant.material2.g; // CORE_BRDF_MIN_ROUGHNESS - 1.0
        CORE_RELAXEDP const float alphaCC = roughnessCC * roughnessCC;
        alpha2CC = alphaCC * alphaCC;
        clearCoat = uObjectPushConstant.material2.r; // 0.0 - 1.0

        // compensate f0 with clear coat
        f0 = mix(f0, f0ClearCoatToSurface(f0), clearCoat);
    }

    ShadingVectors shadingVectors;
    shadingVectors.N = N;
    shadingVectors.NoV = NoV;
    shadingVectors.V = V;
    shadingVectors.faceNormal = normNormal;

    ClearCoatShadingVariables clearCoatShadingVariables;
    clearCoatShadingVariables.alpha2 = alpha2CC;
    clearCoatShadingVariables.clearCoat = clearCoat;

    vec3 color = calcLighting(
        diffuseColor,
        f0,
        alpha2,
        shadingVectors,
        clearCoatShadingVariables);

    const uint camIdx = uObjectPushConstant.indices.z;
    const vec3 worldNormal = normalize(mat3(uCameras[camIdx].viewInv) * N);
    const vec3 worldNormalEnv = mat3(uEnvironment.envRotation) * worldNormal;
    // lambert baked into irradianceSample (SH)
    CORE_RELAXEDP vec3 irradiance = getIrradianceSample(worldNormalEnv) * diffuseColor * ao;

    const vec3 viewReflect = reflect(-V, N);
    const vec3 worldReflect = normalize(mat3(uCameras[camIdx].viewInv) * viewReflect);
    const CORE_RELAXEDP vec3 fIndirect = EnvBRDFApprox(f0, roughness, NoV);
    // ao applied after clear coat
    CORE_RELAXEDP vec3 radiance = getRadianceSample(worldReflect, roughness) * fIndirect;

    if ((CORE_MATERIAL_FLAGS & CORE_MATERIAL_CLEAR_COAT_BIT)
        == CORE_MATERIAL_CLEAR_COAT_BIT) {
        const float NoVCC = clamp(dot(normNormal, V), CORE_PBR_FRAG_EPSILON, 1.0);
        vec3 worldReflectCC = reflect(-V, normNormal);
        worldReflectCC = normalize(mat3(uCameras[camIdx].viewInv) * worldReflectCC); // to world
        const float FCC = fSchlickSingle(0.04, NoVCC) * clearCoat;
        const float attenuationCC = 1.0 - FCC;

        // energy compensation
        irradiance *= attenuationCC;
        radiance *= attenuationCC * attenuationCC;
        // add clear coat radiance
        radiance += getRadianceSample(worldReflectCC, roughnessCC) * FCC;
    }
    // apply ao for indirect specular as well (cheap version)
#if 1
    radiance *= ao * SpecularHorizonOcclusion(viewReflect, normNormal);
#else
    radiance *= EnvSpecularAo(ao, NoV, roughness) * SpecularHorizonOcclusion(viewReflect, normNormal);
#endif

    color += (irradiance + radiance);

    CORE_RELAXEDP vec3 emissive = CORE_TEXTURE_2D(sampler2D(uTexEmissive, uSampler), inUv).xyz * uObjectPushConstant.emissive.rgb;
    color += emissive;

    color.rgb = min(color.rgb, CORE_HDR_FLOAT_CLAMP_MAX_VALUE); // not expecting negative lights
    return vec4(color.rgb, baseColor.a);
}

/*
fragment shader for basic pbr materials.
*/
void main(void)
{
    if (CORE_MATERIAL_TYPE == CORE_MATERAL_UNLIT) {
        outColor = unlitBasic();
    } else if (CORE_MATERIAL_TYPE == CORE_MATERAL_UNLIT_SHADOW_ALPHA) {
        outColor = unlitShadowAlpha();
    } else {
        outColor = pbrBasic();
    }

    if ((CORE_POST_PROCESS_FLAGS & POST_PROCESS_SPECIALIZATION_TONEMAP_BIT) == POST_PROCESS_SPECIALIZATION_TONEMAP_BIT) {
        CORE_RELAXEDP const float exposure = uEnvironment.tonemap.x;
        outColor.rgb = tonemap(outColor.rgb, exposure, CORE_POST_PROCESS_FLAGS);
    }
    if ((CORE_POST_PROCESS_FLAGS & POST_PROCESS_SPECIALIZATION_VIGNETTE_BIT)
        == POST_PROCESS_SPECIALIZATION_VIGNETTE_BIT) {
        vec2 fragUv;
        CORE_GET_FRAGCOORD_UV(fragUv, gl_FragCoord.xy, uEnvironment.viewportSizeInvViewportSize.zw);
        CORE_RELAXEDP const vec2 vignetteValues = uEnvironment.vignette.xy;
        CORE_RELAXEDP const float vignette = getVignetteCoeff(fragUv, 40.0 * vignetteValues.x, vignetteValues.y);
        outColor.rgb *= vignette;
    }
}
