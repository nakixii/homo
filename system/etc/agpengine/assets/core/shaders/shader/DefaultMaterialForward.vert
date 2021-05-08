#version 460 core
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

// includes

#include "core/shaders/common/core_default_camera_structures_common.h"

#include "common/default_material_structures_common.h"

layout(constant_id = 0) const uint CORE_PRIMITIVE_FLAGS = 0;

// sets

layout(set = 0, binding = 0, std140) uniform uCameraMatrices
{
    DefaultCameraMatrixStruct uCameras[CORE_MAX_DEFAULT_CAMERA_COUNT];
};

layout(set = 2, binding = 0, std140) uniform uMeshData
{
    DefaultMaterialMeshStruct uMeshMatrix;
};

layout(set = 2, binding = 1, std140) uniform uObjectSkinData
{
    DefaultMaterialSkinStruct uSkinData;
};

layout(push_constant, std430) uniform uPushConstant
{
    DefaultMaterialPushConstantStruct uObjectPushConstant;
};

// in / out

layout(location = 0) in vec3 inPosition;
layout(location = 1) in vec3 inNormal;
layout(location = 2) in vec2 inUv;
layout(location = 3) in vec4 inTangent;
layout(location = 4) in uvec4 inIndex;
layout(location = 5) in CORE_RELAXEDP vec4 inWeight;
layout(location = 6) in CORE_RELAXEDP vec4 inColor;

layout(location = 0) out vec3 outPos;       // viewspace
layout(location = 1) out CORE_RELAXEDP vec3 outNormal;    // viewspace
layout(location = 2) out CORE_RELAXEDP vec4 outTangentW;  // viewspace
layout(location = 3) out vec4 outShadowCoord;
layout(location = 4) out vec2 outUv;
layout(location = 5) out CORE_RELAXEDP vec4 outColor;

mat4 getWorldMatrix()
{
    if ((CORE_PRIMITIVE_FLAGS & CORE_PRIMITIVE_SKIN_BIT)
        == CORE_PRIMITIVE_SKIN_BIT)
    {
        mat4 worldMatrix = (uSkinData.jointMatrices[inIndex.x] * inWeight.x);
        worldMatrix += (uSkinData.jointMatrices[inIndex.y] * inWeight.y);
        worldMatrix += (uSkinData.jointMatrices[inIndex.z] * inWeight.z);
        worldMatrix += (uSkinData.jointMatrices[inIndex.w] * inWeight.w);
        return uMeshMatrix.world * worldMatrix;
    }
    else
    {
        return uMeshMatrix.world;
    }
}

mat4 getShadowMatrix()
{
    const uint shadowCamIdx = uObjectPushConstant.indices.w;
    return uCameras[shadowCamIdx].shadowViewProj;
}

/*
vertex shader for basic pbr materials.
*/
void main(void)
{
    const uint cameraIdx = uObjectPushConstant.indices.z;
    const mat4 worldMatrix = getWorldMatrix();
    const vec3 worldPos = (worldMatrix * vec4(inPosition.xyz, 1.0)).xyz;
    const mat4 worldView = uCameras[cameraIdx].view * worldMatrix;
    const vec3 viewPos = (worldView * vec4(inPosition.xyz, 1.0)).xyz;

    CORE_VERTEX_OUT(uCameras[cameraIdx].proj * vec4(viewPos, 1.0));

    outPos = viewPos;
    outNormal = normalize(mat3(worldView) * inNormal.xyz);
    if ((CORE_PRIMITIVE_FLAGS & CORE_PRIMITIVE_TANGENTS_BIT)
        == CORE_PRIMITIVE_TANGENTS_BIT)
    {
        outTangentW = vec4(normalize(mat3(worldView) * inTangent.xyz), inTangent.w);
    }
    else
    {
        outTangentW = vec4(0.0, 0.0, 0.0, 1.0);
    }
    outShadowCoord = getShadowMatrix() * vec4(worldPos.xyz, 1.0);
    outUv = inUv;

    if ((CORE_PRIMITIVE_FLAGS & CORE_PRIMITIVE_VERTEX_COLORS_BIT)
        == CORE_PRIMITIVE_VERTEX_COLORS_BIT)
    {
        outColor = inColor;
    }
    else
    {
        outColor = vec4(1.0);
    }
}
