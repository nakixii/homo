#version 460 core
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

// specialization

// includes
#include "core/shaders/common/core_compatibility_common.h"
#include "core/shaders/common/core_blur_common.h"

// sets

layout(set = 0, binding = 0) uniform sampler uSampler;
layout(set = 0, binding = 1) uniform texture2D uTex;

layout(constant_id = 0) const uint CORE_BLUR_COLOR_TYPE = 0;

// in / out

layout (location = 0) in vec2 inUv;

layout (location = 0) out vec4 outColor;

layout(push_constant, std430) uniform uPushConstant
{
    BlurPushConstantStruct uPc;
};

void main(void)
{
    if (CORE_BLUR_COLOR_TYPE == CORE_BLUR_TYPE_R)
    {
        outColor.r = GaussianBlurR(uTex, uSampler, gl_FragCoord.xy, inUv.xy, uPc.dir.xy, uPc.texSizeInvTexSize.zw).r;
    }
    else if (CORE_BLUR_COLOR_TYPE == CORE_BLUR_TYPE_RG)
    {
        outColor.rg = GaussianBlurRG(uTex, uSampler, gl_FragCoord.xy, inUv.xy, uPc.dir.xy, uPc.texSizeInvTexSize.zw).rg;
    }
    else if (CORE_BLUR_COLOR_TYPE == CORE_BLUR_TYPE_RGB)
    {
        outColor.rgb = GaussianBlurRGB(uTex, uSampler, gl_FragCoord.xy, inUv.xy, uPc.dir.xy, uPc.texSizeInvTexSize.zw).rgb;
    }
    else if (CORE_BLUR_COLOR_TYPE == CORE_BLUR_TYPE_A)
    {
        outColor.r = GaussianBlurA(uTex, uSampler, gl_FragCoord.xy, inUv.xy, uPc.dir.xy, uPc.texSizeInvTexSize.zw).r;
    }
    else // (CORE_BLUR_COLOR_TYPE == CORE_BLUR_TYPE_RGBA)
    {
        outColor.rgba = GaussianBlurRGBA(uTex, uSampler, gl_FragCoord.xy, inUv.xy, uPc.dir.xy, uPc.texSizeInvTexSize.zw).rgba;
    }
}
