#version 460 core
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

// includes

#include "core/shaders/common/core_color_conversion_common.h"

#include "core/shaders/common/post_process_common.h"

// sets

layout(set = 0, binding = 0) uniform texture2D uTex;
layout(set = 0, binding = 1) uniform sampler uSampler;

layout(push_constant, std430) uniform uPushConstant
{
    PostProcessTonemapStruct uPostProcessPushConstant;
};

// in / out

layout (location = 0) in vec2 inUv;

layout (location = 0) out vec4 outColor;

#define CORE_ENABLE_SCENE_FRINGE 0
#define CORE_ENABLE_SCENE_VIGNETTE 0

/*
fragment shader for post process and tonemapping
*/
void main(void)
{
    vec4 color = CORE_TEXTURE_2D(sampler2D(uTex, uSampler), inUv);

#if (CORE_ENABLE_SCENE_FRINGE == 1)
    {
        float chroma = getChromaCoeff(inUv, 2.0) * 1.0;

        vec2 uvStep = uPostProcessPushConstant.texSizeInvTexSize.zw;
        vec2 uvDistToImageCenter = chroma * uvStep;
        float chromaRed = CORE_TEXTURE_2D(sampler2D(uTex, uSampler),
            inUv - vec2(uvDistToImageCenter.x, uvDistToImageCenter.y)).x;
        float chromaBlue = CORE_TEXTURE_2D(sampler2D(uTex, uSampler),
            inUv + vec2(uvDistToImageCenter.x, uvDistToImageCenter.y)).z;

        color.r = chromaRed;
        color.b = chromaBlue;
    }
#endif

#if (CORE_ENABLE_SCENE_VIGNETTE == 1)
    const float vignette = getVignetteCoeff(inUv, 20.0, 0.4);
    color.rgb *= vignette;
#endif

    outColor = color;
}
