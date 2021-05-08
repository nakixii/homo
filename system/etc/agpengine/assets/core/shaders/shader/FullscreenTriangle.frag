#version 460 core
#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

// includes

// sets

// in / out
layout(location = 0) in vec2 inUv;

layout (location = 0) out vec4 outColor;

/*

*/
void main(void)
{
    outColor = vec4(inUv, 0.0, 1.0);
}
