#version 460 core
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

// includes
#include "core/shaders/common/core_compatibility_common.h"

// sets

struct ImguiPushConstantStruct
{
    vec4 scaleTranslate; // .xy = scale, .zw = translate
};

layout(push_constant, std430) uniform uPushConstant
{
    ImguiPushConstantStruct uPc;
};

// in / out

layout(location = 0) in vec2 inPosition;
layout(location = 1) in vec2 inUv;
layout(location = 2) in vec4 inColor;

layout(location = 0) out vec4 outColor;
layout(location = 1) out vec2 outUv;

/*
vertex shader for imgui
*/
void main(void)
{
    outUv = inUv;
    outColor = inColor;
    CORE_VERTEX_OUT(vec4(inPosition.xy * uPc.scaleTranslate.xy + uPc.scaleTranslate.zw, 0.0, 1.0));
}
