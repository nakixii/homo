#version 460 core
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

// includes

#include "common/bloom_common.h"

// sets

layout(set = 0, binding = 0) uniform sampler uSampler;

layout(set = 1, binding = 0) uniform texture2D uTex;

layout (input_attachment_index = 0, set = 1, binding = 1) uniform subpassInput uInputColor;

layout(push_constant, std430) uniform uPushConstant
{
    BloomPushConstantStruct uPc;
};

// in / out

layout (location = 0) in vec2 inUv;

layout (location = 0) out vec4 outColor;

///////////////////////////////////////////////////////////////////////////////
// bloom upscale

void main()
{
    const vec2 uv = inUv;

    vec3 color = bloomUpscale(uv, uPc.texSizeInvTexSize.zw, uTex, uSampler);

    const vec3 baseColor = subpassLoad(uInputColor).rgb;
    color = min((color + baseColor), CORE_BLOOM_CLAMP_MAX_VALUE);

    outColor = vec4(color, 1.0);
}

