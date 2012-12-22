#ifndef _XENON_MACROS_FXH_
#define _XENON_MACROS_FXH_


#define _NO_FIXED_FUNCTION_

// ----------------------------------------------------------------------------
// SAMPLER MACROS
// ----------------------------------------------------------------------------
#define SAMPLER_2D_BEGIN(samplerName, annotations) \
	sampler2D samplerName \
	< \
		annotations \
	> = sampler_state \
	{
		
#define SAMPLER_2D_END };

#define SAMPLER( samplerName )	samplerName

#define SAMPLER_CUBE_BEGIN(samplerName, annotations) \
	samplerCUBE samplerName \
	< \
		annotations \
	> = sampler_state \
	{
		
#define SAMPLER_CUBE_END };

#define SAMPLER_3D_BEGIN(samplerName, annotations) \
	sampler3D samplerName \
	< \
		annotations \
	> = sampler_state \
	{
		
#define SAMPLER_3D_END };

// ----------------------------------------------------------------------------
// SHADER VERSIONS
// ----------------------------------------------------------------------------
#define VS_VERSION				vs_3_0
#define VS_VERSION_ULTRAHIGH	vs_3_0
#define VS_VERSION_HIGH			vs_3_0
#define VS_VERSION_LOW			vs_3_0

#define PS_VERSION				ps_3_0
#define PS_VERSION_ULTRAHIGH	ps_3_0
#define PS_VERSION_HIGH			ps_3_0
#define PS_VERSION_LOW			ps_3_0

// ----------------------------------------------------------------------------
// FILTERS
// ----------------------------------------------------------------------------
#define MinFilterBest Anisotropic 
#define MagFilterBest Linear 	
#define MipFilterBest Linear 

// ----------------------------------------------------------------------------
// RENDERSTATE ENUMS
// ----------------------------------------------------------------------------

// Taken from d3d9types.h D3DBLEND enum
static const int D3DBLEND_ZERO               = 0;
static const int D3DBLEND_ONE                = 1;
static const int D3DBLEND_SRCCOLOR           = 4;
static const int D3DBLEND_INVSRCCOLOR        = 5;
static const int D3DBLEND_SRCALPHA           = 6;
static const int D3DBLEND_INVSRCALPHA        = 7;
static const int D3DBLEND_DESTCOLOR          = 8;
static const int D3DBLEND_INVDESTCOLOR       = 9;
static const int D3DBLEND_DESTALPHA          = 10;
static const int D3DBLEND_INVDESTALPHA       = 11;
static const int D3DBLEND_BLENDFACTOR        = 12;
static const int D3DBLEND_INVBLENDFACTOR     = 13;
static const int D3DBLEND_CONSTANTALPHA      = 14;  // Xbox 360 extension
static const int D3DBLEND_INVCONSTANTALPHA   = 15;  // Xbox 360 extension
static const int D3DBLEND_SRCALPHASAT        = 16;
// The following are not supported on Xbox 360:
//
// D3DBLEND_BOTHSRCALPHA
// D3DBLEND_BOTHINVSRCALPHA

// Taken from d3d9types.h D3DCULL enum
static const int D3DCULL_NONE                = 0x0;
static const int D3DCULL_CW                  = 0x2;
static const int D3DCULL_CCW                 = 0x6;

// Taken from d3d9types.h D3DCMPFUNC enum
static const int D3DCMP_NEVER                = 0;
static const int D3DCMP_LESS                 = 1;
static const int D3DCMP_EQUAL                = 2;
static const int D3DCMP_LESSEQUAL            = 3;
static const int D3DCMP_GREATER              = 4;
static const int D3DCMP_NOTEQUAL             = 5;
static const int D3DCMP_GREATEREQUAL         = 6;
static const int D3DCMP_ALWAYS               = 7;

// Taken from d3d9types.h. Flags to construct D3DRS_COLORWRITEENABLE
static const int D3DCOLORWRITEENABLE_RED     = 1; //(1L<<0)
static const int D3DCOLORWRITEENABLE_GREEN   = 2; //(1L<<1)
static const int D3DCOLORWRITEENABLE_BLUE    = 4; //(1L<<2)
static const int D3DCOLORWRITEENABLE_ALPHA   = 8; //(1L<<3)
static const int D3DCOLORWRITEENABLE_ALL     = 0xf;     // Xbox 360 extension [LLatta 2006-09-06: Copied to Windows version too]

#endif // include guard

