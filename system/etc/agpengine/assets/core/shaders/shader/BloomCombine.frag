#version 460 core
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

// includes

#include "common/bloom_common.h"

// sets

layout(set = 0, binding = 0) uniform sampler uSampler;

layout(set = 1, binding = 0) uniform texture2D uTex;
layout(set = 1, binding = 1) uniform texture2D uTexBloom;

layout(push_constant, std430) uniform uPushConstant
{
    BloomPushConstantStruct uPc;
};

// in / out

layout (location = 0) in vec2 inUv;

layout (location = 0) out vec4 outColor;

///////////////////////////////////////////////////////////////////////////////
// bloom combine

void main()
{
    const vec2 uv = inUv;
    const vec3 baseColor = CORE_TEXTURE_2D(sampler2D(uTex, uSampler), uv).xyz;
    // TODO: more samples (lower resolution)
    const vec3 bloomColor = CORE_TEXTURE_2D(sampler2D(uTexBloom, uSampler), uv).xyz;

    vec3 finalColor = min(bloomCombine(baseColor, bloomColor, uPc.bloomParameters), CORE_BLOOM_CLAMP_MAX_VALUE);
    outColor = vec4(finalColor, 1.0);
}
