#version 460 core
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

#define CORE_ENABLE_INPUT_ATTACHMENT 1

// specialization

// includes

#include "core/shaders/common/core_color_conversion_common.h"

#include "core/shaders/common/tonemap_common.h"

// sets

#if (CORE_ENABLE_INPUT_ATTACHMENT == 1)
layout(input_attachment_index = 0, set = 0, binding = 0) uniform subpassInput uTex;
#else
layout(set = 0, binding = 0) uniform texture2D uTex;
#endif
layout(set = 0, binding = 1) uniform sampler uSampler;

// in / out

layout (location = 0) in vec2 inUv;

layout (location = 0) out vec4 outColor;
layout (location = 1) out vec4 outColorAlpha;

/*
fragment shader for tonemapping HDR and setting luma to alpha channel for e.g. FXAA
*/
void main(void)
{
#if (CORE_ENABLE_INPUT_ATTACHMENT == 1)
    vec4 color = subpassLoad(uTex);
#else
    vec4 color = CORE_TEXTURE_2D(sampler2D(uTex, uSampler), inUv);
#endif

    const float exposure = 0.7;
    const uint postProcessFlags = POST_PROCESS_SPECIALIZATION_TONEMAP_TYPE_ACES_BIT;
    color.rgb = tonemap(color.rgb, exposure, postProcessFlags);

    const float luma = CalcLuma(color.rgb);

    outColor = vec4(color.rgb, luma);
    outColorAlpha = color.aaaa;
}
