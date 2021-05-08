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
    DefaultCameraMatrixStruct uCamera[CORE_MAX_DEFAULT_CAMERA_COUNT];
};

layout(set = 1, binding = 0, std140) uniform uMeshData
{
    DefaultMaterialMeshStruct uMeshMatrix;
};

layout(set = 1, binding = 1, std140) uniform uObjectSkinData
{
    DefaultMaterialSkinStruct uSkinData;
};

layout(push_constant, std430) uniform uPushConstant
{
    DefaultMaterialDepthPassPushConstantStruct uObjectPushConstant;
};

// in / out

layout(location = 0) in vec3 inPosition;
layout(location = 1) in uvec4 inIndex;
layout(location = 2) in vec4 inWeight;

mat4 getWorldMatrix()
{
    const uint meshIndex = uObjectPushConstant.indices.y;
    if ((CORE_PRIMITIVE_FLAGS & CORE_PRIMITIVE_SKIN_BIT) == CORE_PRIMITIVE_SKIN_BIT)
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

/*
vertex shader for basic depth pass.
*/
void main(void)
{
    const mat4 worldMatrix = getWorldMatrix();
    const uint cameraIdx = uObjectPushConstant.indices.z;
    CORE_VERTEX_OUT(uCamera[cameraIdx].viewProj * worldMatrix * vec4(inPosition, 1.0));
}
