#version 460 core
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

// includes
#include "core/shaders/common/core_compatibility_common.h"
// sets

layout(set = 0, binding = 0) uniform texture2D uTex;
layout(set = 0, binding = 1) uniform sampler uSampler;

// in / out

layout (location = 0) in vec4 inColor;
layout (location = 1) in vec2 inUv;

layout (location = 0) out vec4 outColor;

/*
fragment shader for Imgui
*/
void main(void)
{
    outColor = inColor * CORE_TEXTURE_2D(sampler2D(uTex, uSampler), inUv.xy);
}
