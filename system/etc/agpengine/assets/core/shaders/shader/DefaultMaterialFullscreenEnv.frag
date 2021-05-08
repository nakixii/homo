#version 460 core
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

// includes

#include "core/shaders/common/core_default_camera_structures_common.h"

#include "common/default_material_env_structures_common.h"
#include "common/default_material_structures_common.h"
#include "common/lighting_common.h"
#include "core/shaders/common/tonemap_common.h"

// sets

layout(set = 0, binding = 0, std140) uniform uCameraMatrices
{
    DefaultCameraMatrixStruct uCamera;
};

layout(set = 1, binding = 0) uniform texture2D uTex;
layout(set = 1, binding = 1) uniform textureCube uTexCube;
layout(set = 1, binding = 2) uniform sampler uSampler;

layout(push_constant, std430) uniform uPushConstant
{
    DefaultMaterialEnvPushConstantStruct uEnvPushConstant;
};

layout(constant_id = 0) const uint CORE_DEFAULT_ENV_TYPE = 0;
layout(constant_id = 1) const uint CORE_POST_PROCESS_FLAGS = 0;

// in / out

layout (location = 0) in vec2 inUv;

layout (location = 0) out vec4 outColor;

#define CORE_DEFAULT_ENV_PI 3.1415926535897932384626433832795

/*
fragment shader for environment sampling
*/
void main(void)
{
    vec3 color = vec3(0.0);

    const float lodLevel = uEnvPushConstant.envColorFactor.a;
    if ((CORE_DEFAULT_ENV_TYPE == CORE_BACKGROUND_TYPE_CUBEMAP) ||
        (CORE_DEFAULT_ENV_TYPE == CORE_BACKGROUND_TYPE_EQUIRECTANGULAR)) {

        // NOTE: would be nicer to calculate in the vertex shader

        // remove translation from component
        mat4 viewProjInv = uCamera.viewInv;
        viewProjInv[3] = vec4(0.0, 0.0, 0.0, 1.0);
        viewProjInv = viewProjInv * uCamera.projInv;

        vec4 farPlane = viewProjInv * vec4(inUv.x, inUv.y, 1.0, 1.0);
        farPlane.xyz = farPlane.xyz / farPlane.w;

        vec4 nearPlane = viewProjInv * vec4(inUv.x, inUv.y, 0.0, 1.0);
        nearPlane.xyz = nearPlane.xyz / nearPlane.w;

        const vec3 worldView = mat3(uEnvPushConstant.envRotation) * normalize(farPlane.xyz - nearPlane.xyz);

        if (CORE_DEFAULT_ENV_TYPE == CORE_BACKGROUND_TYPE_CUBEMAP) {
            color = unpackEnvMap(CORE_TEXTURE_LOD_CUBE(samplerCube(uTexCube, uSampler), worldView, lodLevel));
        } else {
            const vec2 texCoord = vec2(atan(worldView.z, worldView.x) + CORE_DEFAULT_ENV_PI,
                acos(worldView.y)) / vec2(2.0 * CORE_DEFAULT_ENV_PI, CORE_DEFAULT_ENV_PI);
            color = CORE_TEXTURE_LOD_2D(sampler2D(uTex, uSampler), texCoord, lodLevel).xyz;
        }
    } else if (CORE_DEFAULT_ENV_TYPE == CORE_BACKGROUND_TYPE_IMAGE) {
        const vec2 texCoord = (inUv + vec2(1.0)) * 0.5;
        color = unpackEnvMap(CORE_TEXTURE_LOD_2D(sampler2D(uTex, uSampler), texCoord, lodLevel));
    }

    color *= uEnvPushConstant.envColorFactor.xyz;

    if ((CORE_POST_PROCESS_FLAGS & POST_PROCESS_SPECIALIZATION_TONEMAP_BIT)
        == POST_PROCESS_SPECIALIZATION_TONEMAP_BIT) {
        const float exposure = uEnvPushConstant.tonemap.x;
        color.rgb = tonemap(color, exposure, CORE_POST_PROCESS_FLAGS);
    }
    if ((CORE_POST_PROCESS_FLAGS & POST_PROCESS_SPECIALIZATION_VIGNETTE_BIT)
        == POST_PROCESS_SPECIALIZATION_VIGNETTE_BIT) {
        vec2 fragUv;
        CORE_GET_FRAGCOORD_UV(fragUv, gl_FragCoord.xy, uEnvPushConstant.viewportSizeInvViewportSize.zw);
        CORE_RELAXEDP const vec2 vignetteValues = uEnvPushConstant.vignette.xy;
        CORE_RELAXEDP const float vignette = getVignetteCoeff(fragUv, 40.0 * vignetteValues.x, vignetteValues.y);
        color.rgb *= vignette;
    }

    outColor = vec4(color.xyz, 1.0);
}
