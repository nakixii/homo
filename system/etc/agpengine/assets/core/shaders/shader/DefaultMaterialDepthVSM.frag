#version 460 core
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

// includes
#include "core/shaders/common/core_compatibility_common.h"

// sets

// in / out

layout (location = 0) out vec4 outColor;

//layout (depth_unchanged) out float gl_FragDepth;

#define CORE_ADJUST_VSM_MOMENTS 1

/*
fragment shader for VSM depth pass.
*/
void main(void)
{
    const float moment1 = gl_FragCoord.z;
    float moment2 = moment1 * moment1;

#if (CORE_ADJUST_VSM_MOMENTS == 1)
    // adjust moments
    float dx = dFdx(moment1);
    float dy = dFdy(moment1);
    moment2 += 0.25*(dx*dx+dy*dy);
#endif

    outColor = vec4(moment1, moment2, 0.0, 0.0);
}
