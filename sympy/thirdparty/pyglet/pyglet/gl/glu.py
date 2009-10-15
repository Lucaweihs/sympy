# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2007 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------
'''Wrapper for /usr/include/GL/glu.h

Generated by tools/gengl.py.
Do not modify this file.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: glu.py 878 2007-06-09 04:58:51Z Alex.Holkner $'

from ctypes import *
from pyglet.gl.lib import link_GLU as _link_function
from pyglet.gl.lib import c_ptrdiff_t

# BEGIN GENERATED CONTENT (do not edit below this line)

# This content is generated by tools/gengl.py.
# Wrapper for /usr/include/GL/glu.h


GLU_EXT_object_space_tess = 1 	# /usr/include/GL/glu.h:58
GLU_EXT_nurbs_tessellator = 1 	# /usr/include/GL/glu.h:59
GLU_FALSE = 0 	# /usr/include/GL/glu.h:62
GLU_TRUE = 1 	# /usr/include/GL/glu.h:63
GLU_VERSION_1_1 = 1 	# /usr/include/GL/glu.h:66
GLU_VERSION_1_2 = 1 	# /usr/include/GL/glu.h:67
GLU_VERSION_1_3 = 1 	# /usr/include/GL/glu.h:68
GLU_VERSION = 100800 	# /usr/include/GL/glu.h:71
GLU_EXTENSIONS = 100801 	# /usr/include/GL/glu.h:72
GLU_INVALID_ENUM = 100900 	# /usr/include/GL/glu.h:75
GLU_INVALID_VALUE = 100901 	# /usr/include/GL/glu.h:76
GLU_OUT_OF_MEMORY = 100902 	# /usr/include/GL/glu.h:77
GLU_INCOMPATIBLE_GL_VERSION = 100903 	# /usr/include/GL/glu.h:78
GLU_INVALID_OPERATION = 100904 	# /usr/include/GL/glu.h:79
GLU_OUTLINE_POLYGON = 100240 	# /usr/include/GL/glu.h:83
GLU_OUTLINE_PATCH = 100241 	# /usr/include/GL/glu.h:84
GLU_NURBS_ERROR = 100103 	# /usr/include/GL/glu.h:87
GLU_ERROR = 100103 	# /usr/include/GL/glu.h:88
GLU_NURBS_BEGIN = 100164 	# /usr/include/GL/glu.h:89
GLU_NURBS_BEGIN_EXT = 100164 	# /usr/include/GL/glu.h:90
GLU_NURBS_VERTEX = 100165 	# /usr/include/GL/glu.h:91
GLU_NURBS_VERTEX_EXT = 100165 	# /usr/include/GL/glu.h:92
GLU_NURBS_NORMAL = 100166 	# /usr/include/GL/glu.h:93
GLU_NURBS_NORMAL_EXT = 100166 	# /usr/include/GL/glu.h:94
GLU_NURBS_COLOR = 100167 	# /usr/include/GL/glu.h:95
GLU_NURBS_COLOR_EXT = 100167 	# /usr/include/GL/glu.h:96
GLU_NURBS_TEXTURE_COORD = 100168 	# /usr/include/GL/glu.h:97
GLU_NURBS_TEX_COORD_EXT = 100168 	# /usr/include/GL/glu.h:98
GLU_NURBS_END = 100169 	# /usr/include/GL/glu.h:99
GLU_NURBS_END_EXT = 100169 	# /usr/include/GL/glu.h:100
GLU_NURBS_BEGIN_DATA = 100170 	# /usr/include/GL/glu.h:101
GLU_NURBS_BEGIN_DATA_EXT = 100170 	# /usr/include/GL/glu.h:102
GLU_NURBS_VERTEX_DATA = 100171 	# /usr/include/GL/glu.h:103
GLU_NURBS_VERTEX_DATA_EXT = 100171 	# /usr/include/GL/glu.h:104
GLU_NURBS_NORMAL_DATA = 100172 	# /usr/include/GL/glu.h:105
GLU_NURBS_NORMAL_DATA_EXT = 100172 	# /usr/include/GL/glu.h:106
GLU_NURBS_COLOR_DATA = 100173 	# /usr/include/GL/glu.h:107
GLU_NURBS_COLOR_DATA_EXT = 100173 	# /usr/include/GL/glu.h:108
GLU_NURBS_TEXTURE_COORD_DATA = 100174 	# /usr/include/GL/glu.h:109
GLU_NURBS_TEX_COORD_DATA_EXT = 100174 	# /usr/include/GL/glu.h:110
GLU_NURBS_END_DATA = 100175 	# /usr/include/GL/glu.h:111
GLU_NURBS_END_DATA_EXT = 100175 	# /usr/include/GL/glu.h:112
GLU_NURBS_ERROR1 = 100251 	# /usr/include/GL/glu.h:115
GLU_NURBS_ERROR2 = 100252 	# /usr/include/GL/glu.h:116
GLU_NURBS_ERROR3 = 100253 	# /usr/include/GL/glu.h:117
GLU_NURBS_ERROR4 = 100254 	# /usr/include/GL/glu.h:118
GLU_NURBS_ERROR5 = 100255 	# /usr/include/GL/glu.h:119
GLU_NURBS_ERROR6 = 100256 	# /usr/include/GL/glu.h:120
GLU_NURBS_ERROR7 = 100257 	# /usr/include/GL/glu.h:121
GLU_NURBS_ERROR8 = 100258 	# /usr/include/GL/glu.h:122
GLU_NURBS_ERROR9 = 100259 	# /usr/include/GL/glu.h:123
GLU_NURBS_ERROR10 = 100260 	# /usr/include/GL/glu.h:124
GLU_NURBS_ERROR11 = 100261 	# /usr/include/GL/glu.h:125
GLU_NURBS_ERROR12 = 100262 	# /usr/include/GL/glu.h:126
GLU_NURBS_ERROR13 = 100263 	# /usr/include/GL/glu.h:127
GLU_NURBS_ERROR14 = 100264 	# /usr/include/GL/glu.h:128
GLU_NURBS_ERROR15 = 100265 	# /usr/include/GL/glu.h:129
GLU_NURBS_ERROR16 = 100266 	# /usr/include/GL/glu.h:130
GLU_NURBS_ERROR17 = 100267 	# /usr/include/GL/glu.h:131
GLU_NURBS_ERROR18 = 100268 	# /usr/include/GL/glu.h:132
GLU_NURBS_ERROR19 = 100269 	# /usr/include/GL/glu.h:133
GLU_NURBS_ERROR20 = 100270 	# /usr/include/GL/glu.h:134
GLU_NURBS_ERROR21 = 100271 	# /usr/include/GL/glu.h:135
GLU_NURBS_ERROR22 = 100272 	# /usr/include/GL/glu.h:136
GLU_NURBS_ERROR23 = 100273 	# /usr/include/GL/glu.h:137
GLU_NURBS_ERROR24 = 100274 	# /usr/include/GL/glu.h:138
GLU_NURBS_ERROR25 = 100275 	# /usr/include/GL/glu.h:139
GLU_NURBS_ERROR26 = 100276 	# /usr/include/GL/glu.h:140
GLU_NURBS_ERROR27 = 100277 	# /usr/include/GL/glu.h:141
GLU_NURBS_ERROR28 = 100278 	# /usr/include/GL/glu.h:142
GLU_NURBS_ERROR29 = 100279 	# /usr/include/GL/glu.h:143
GLU_NURBS_ERROR30 = 100280 	# /usr/include/GL/glu.h:144
GLU_NURBS_ERROR31 = 100281 	# /usr/include/GL/glu.h:145
GLU_NURBS_ERROR32 = 100282 	# /usr/include/GL/glu.h:146
GLU_NURBS_ERROR33 = 100283 	# /usr/include/GL/glu.h:147
GLU_NURBS_ERROR34 = 100284 	# /usr/include/GL/glu.h:148
GLU_NURBS_ERROR35 = 100285 	# /usr/include/GL/glu.h:149
GLU_NURBS_ERROR36 = 100286 	# /usr/include/GL/glu.h:150
GLU_NURBS_ERROR37 = 100287 	# /usr/include/GL/glu.h:151
GLU_AUTO_LOAD_MATRIX = 100200 	# /usr/include/GL/glu.h:154
GLU_CULLING = 100201 	# /usr/include/GL/glu.h:155
GLU_SAMPLING_TOLERANCE = 100203 	# /usr/include/GL/glu.h:156
GLU_DISPLAY_MODE = 100204 	# /usr/include/GL/glu.h:157
GLU_PARAMETRIC_TOLERANCE = 100202 	# /usr/include/GL/glu.h:158
GLU_SAMPLING_METHOD = 100205 	# /usr/include/GL/glu.h:159
GLU_U_STEP = 100206 	# /usr/include/GL/glu.h:160
GLU_V_STEP = 100207 	# /usr/include/GL/glu.h:161
GLU_NURBS_MODE = 100160 	# /usr/include/GL/glu.h:162
GLU_NURBS_MODE_EXT = 100160 	# /usr/include/GL/glu.h:163
GLU_NURBS_TESSELLATOR = 100161 	# /usr/include/GL/glu.h:164
GLU_NURBS_TESSELLATOR_EXT = 100161 	# /usr/include/GL/glu.h:165
GLU_NURBS_RENDERER = 100162 	# /usr/include/GL/glu.h:166
GLU_NURBS_RENDERER_EXT = 100162 	# /usr/include/GL/glu.h:167
GLU_OBJECT_PARAMETRIC_ERROR = 100208 	# /usr/include/GL/glu.h:170
GLU_OBJECT_PARAMETRIC_ERROR_EXT = 100208 	# /usr/include/GL/glu.h:171
GLU_OBJECT_PATH_LENGTH = 100209 	# /usr/include/GL/glu.h:172
GLU_OBJECT_PATH_LENGTH_EXT = 100209 	# /usr/include/GL/glu.h:173
GLU_PATH_LENGTH = 100215 	# /usr/include/GL/glu.h:174
GLU_PARAMETRIC_ERROR = 100216 	# /usr/include/GL/glu.h:175
GLU_DOMAIN_DISTANCE = 100217 	# /usr/include/GL/glu.h:176
GLU_MAP1_TRIM_2 = 100210 	# /usr/include/GL/glu.h:179
GLU_MAP1_TRIM_3 = 100211 	# /usr/include/GL/glu.h:180
GLU_POINT = 100010 	# /usr/include/GL/glu.h:183
GLU_LINE = 100011 	# /usr/include/GL/glu.h:184
GLU_FILL = 100012 	# /usr/include/GL/glu.h:185
GLU_SILHOUETTE = 100013 	# /usr/include/GL/glu.h:186
GLU_SMOOTH = 100000 	# /usr/include/GL/glu.h:192
GLU_FLAT = 100001 	# /usr/include/GL/glu.h:193
GLU_NONE = 100002 	# /usr/include/GL/glu.h:194
GLU_OUTSIDE = 100020 	# /usr/include/GL/glu.h:197
GLU_INSIDE = 100021 	# /usr/include/GL/glu.h:198
GLU_TESS_BEGIN = 100100 	# /usr/include/GL/glu.h:201
GLU_BEGIN = 100100 	# /usr/include/GL/glu.h:202
GLU_TESS_VERTEX = 100101 	# /usr/include/GL/glu.h:203
GLU_VERTEX = 100101 	# /usr/include/GL/glu.h:204
GLU_TESS_END = 100102 	# /usr/include/GL/glu.h:205
GLU_END = 100102 	# /usr/include/GL/glu.h:206
GLU_TESS_ERROR = 100103 	# /usr/include/GL/glu.h:207
GLU_TESS_EDGE_FLAG = 100104 	# /usr/include/GL/glu.h:208
GLU_EDGE_FLAG = 100104 	# /usr/include/GL/glu.h:209
GLU_TESS_COMBINE = 100105 	# /usr/include/GL/glu.h:210
GLU_TESS_BEGIN_DATA = 100106 	# /usr/include/GL/glu.h:211
GLU_TESS_VERTEX_DATA = 100107 	# /usr/include/GL/glu.h:212
GLU_TESS_END_DATA = 100108 	# /usr/include/GL/glu.h:213
GLU_TESS_ERROR_DATA = 100109 	# /usr/include/GL/glu.h:214
GLU_TESS_EDGE_FLAG_DATA = 100110 	# /usr/include/GL/glu.h:215
GLU_TESS_COMBINE_DATA = 100111 	# /usr/include/GL/glu.h:216
GLU_CW = 100120 	# /usr/include/GL/glu.h:219
GLU_CCW = 100121 	# /usr/include/GL/glu.h:220
GLU_INTERIOR = 100122 	# /usr/include/GL/glu.h:221
GLU_EXTERIOR = 100123 	# /usr/include/GL/glu.h:222
GLU_UNKNOWN = 100124 	# /usr/include/GL/glu.h:223
GLU_TESS_WINDING_RULE = 100140 	# /usr/include/GL/glu.h:226
GLU_TESS_BOUNDARY_ONLY = 100141 	# /usr/include/GL/glu.h:227
GLU_TESS_TOLERANCE = 100142 	# /usr/include/GL/glu.h:228
GLU_TESS_ERROR1 = 100151 	# /usr/include/GL/glu.h:231
GLU_TESS_ERROR2 = 100152 	# /usr/include/GL/glu.h:232
GLU_TESS_ERROR3 = 100153 	# /usr/include/GL/glu.h:233
GLU_TESS_ERROR4 = 100154 	# /usr/include/GL/glu.h:234
GLU_TESS_ERROR5 = 100155 	# /usr/include/GL/glu.h:235
GLU_TESS_ERROR6 = 100156 	# /usr/include/GL/glu.h:236
GLU_TESS_ERROR7 = 100157 	# /usr/include/GL/glu.h:237
GLU_TESS_ERROR8 = 100158 	# /usr/include/GL/glu.h:238
GLU_TESS_MISSING_BEGIN_POLYGON = 100151 	# /usr/include/GL/glu.h:239
GLU_TESS_MISSING_BEGIN_CONTOUR = 100152 	# /usr/include/GL/glu.h:240
GLU_TESS_MISSING_END_POLYGON = 100153 	# /usr/include/GL/glu.h:241
GLU_TESS_MISSING_END_CONTOUR = 100154 	# /usr/include/GL/glu.h:242
GLU_TESS_COORD_TOO_LARGE = 100155 	# /usr/include/GL/glu.h:243
GLU_TESS_NEED_COMBINE_CALLBACK = 100156 	# /usr/include/GL/glu.h:244
GLU_TESS_WINDING_ODD = 100130 	# /usr/include/GL/glu.h:247
GLU_TESS_WINDING_NONZERO = 100131 	# /usr/include/GL/glu.h:248
GLU_TESS_WINDING_POSITIVE = 100132 	# /usr/include/GL/glu.h:249
GLU_TESS_WINDING_NEGATIVE = 100133 	# /usr/include/GL/glu.h:250
GLU_TESS_WINDING_ABS_GEQ_TWO = 100134 	# /usr/include/GL/glu.h:251
class struct_GLUnurbs(Structure):
    __slots__ = [
    ]
struct_GLUnurbs._fields_ = [
    ('_opaque_struct', c_int)
]

GLUnurbs = struct_GLUnurbs 	# /usr/include/GL/glu.h:261
class struct_GLUquadric(Structure):
    __slots__ = [
    ]
struct_GLUquadric._fields_ = [
    ('_opaque_struct', c_int)
]

GLUquadric = struct_GLUquadric 	# /usr/include/GL/glu.h:262
class struct_GLUtesselator(Structure):
    __slots__ = [
    ]
struct_GLUtesselator._fields_ = [
    ('_opaque_struct', c_int)
]

GLUtesselator = struct_GLUtesselator 	# /usr/include/GL/glu.h:263
GLUnurbsObj = GLUnurbs 	# /usr/include/GL/glu.h:266
GLUquadricObj = GLUquadric 	# /usr/include/GL/glu.h:267
GLUtesselatorObj = GLUtesselator 	# /usr/include/GL/glu.h:268
GLUtriangulatorObj = GLUtesselator 	# /usr/include/GL/glu.h:269
GLU_TESS_MAX_COORD = 9.9999999999999998e+149 	# /usr/include/GL/glu.h:271
_GLUfuncptr = CFUNCTYPE(None) 	# /usr/include/GL/glu.h:274
# /usr/include/GL/glu.h:276
gluBeginCurve = _link_function('gluBeginCurve', None, [POINTER(GLUnurbs)], None)

# /usr/include/GL/glu.h:277
gluBeginPolygon = _link_function('gluBeginPolygon', None, [POINTER(GLUtesselator)], None)

# /usr/include/GL/glu.h:278
gluBeginSurface = _link_function('gluBeginSurface', None, [POINTER(GLUnurbs)], None)

# /usr/include/GL/glu.h:279
gluBeginTrim = _link_function('gluBeginTrim', None, [POINTER(GLUnurbs)], None)

GLint = c_int 	# /usr/include/GL/gl.h:58
GLenum = c_uint 	# /usr/include/GL/gl.h:53
GLsizei = c_int 	# /usr/include/GL/gl.h:59
# /usr/include/GL/glu.h:280
gluBuild1DMipmapLevels = _link_function('gluBuild1DMipmapLevels', GLint, [GLenum, GLint, GLsizei, GLenum, GLenum, GLint, GLint, GLint, POINTER(None)], None)

# /usr/include/GL/glu.h:281
gluBuild1DMipmaps = _link_function('gluBuild1DMipmaps', GLint, [GLenum, GLint, GLsizei, GLenum, GLenum, POINTER(None)], None)

# /usr/include/GL/glu.h:282
gluBuild2DMipmapLevels = _link_function('gluBuild2DMipmapLevels', GLint, [GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, GLint, GLint, GLint, POINTER(None)], None)

# /usr/include/GL/glu.h:283
gluBuild2DMipmaps = _link_function('gluBuild2DMipmaps', GLint, [GLenum, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(None)], None)

# /usr/include/GL/glu.h:284
gluBuild3DMipmapLevels = _link_function('gluBuild3DMipmapLevels', GLint, [GLenum, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, GLint, GLint, GLint, POINTER(None)], None)

# /usr/include/GL/glu.h:285
gluBuild3DMipmaps = _link_function('gluBuild3DMipmaps', GLint, [GLenum, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, POINTER(None)], None)

GLboolean = c_ubyte 	# /usr/include/GL/gl.h:54
GLubyte = c_ubyte 	# /usr/include/GL/gl.h:60
# /usr/include/GL/glu.h:286
gluCheckExtension = _link_function('gluCheckExtension', GLboolean, [POINTER(GLubyte), POINTER(GLubyte)], None)

GLdouble = c_double 	# /usr/include/GL/gl.h:65
# /usr/include/GL/glu.h:287
gluCylinder = _link_function('gluCylinder', None, [POINTER(GLUquadric), GLdouble, GLdouble, GLdouble, GLint, GLint], None)

# /usr/include/GL/glu.h:288
gluDeleteNurbsRenderer = _link_function('gluDeleteNurbsRenderer', None, [POINTER(GLUnurbs)], None)

# /usr/include/GL/glu.h:289
gluDeleteQuadric = _link_function('gluDeleteQuadric', None, [POINTER(GLUquadric)], None)

# /usr/include/GL/glu.h:290
gluDeleteTess = _link_function('gluDeleteTess', None, [POINTER(GLUtesselator)], None)

# /usr/include/GL/glu.h:291
gluDisk = _link_function('gluDisk', None, [POINTER(GLUquadric), GLdouble, GLdouble, GLint, GLint], None)

# /usr/include/GL/glu.h:292
gluEndCurve = _link_function('gluEndCurve', None, [POINTER(GLUnurbs)], None)

# /usr/include/GL/glu.h:293
gluEndPolygon = _link_function('gluEndPolygon', None, [POINTER(GLUtesselator)], None)

# /usr/include/GL/glu.h:294
gluEndSurface = _link_function('gluEndSurface', None, [POINTER(GLUnurbs)], None)

# /usr/include/GL/glu.h:295
gluEndTrim = _link_function('gluEndTrim', None, [POINTER(GLUnurbs)], None)

# /usr/include/GL/glu.h:296
gluErrorString = _link_function('gluErrorString', POINTER(GLubyte), [GLenum], None)

GLfloat = c_float 	# /usr/include/GL/gl.h:63
# /usr/include/GL/glu.h:297
gluGetNurbsProperty = _link_function('gluGetNurbsProperty', None, [POINTER(GLUnurbs), GLenum, POINTER(GLfloat)], None)

# /usr/include/GL/glu.h:298
gluGetString = _link_function('gluGetString', POINTER(GLubyte), [GLenum], None)

# /usr/include/GL/glu.h:299
gluGetTessProperty = _link_function('gluGetTessProperty', None, [POINTER(GLUtesselator), GLenum, POINTER(GLdouble)], None)

# /usr/include/GL/glu.h:300
gluLoadSamplingMatrices = _link_function('gluLoadSamplingMatrices', None, [POINTER(GLUnurbs), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLint)], None)

# /usr/include/GL/glu.h:301
gluLookAt = _link_function('gluLookAt', None, [GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble], None)

# /usr/include/GL/glu.h:302
gluNewNurbsRenderer = _link_function('gluNewNurbsRenderer', POINTER(GLUnurbs), [], None)

# /usr/include/GL/glu.h:303
gluNewQuadric = _link_function('gluNewQuadric', POINTER(GLUquadric), [], None)

# /usr/include/GL/glu.h:304
gluNewTess = _link_function('gluNewTess', POINTER(GLUtesselator), [], None)

# /usr/include/GL/glu.h:305
gluNextContour = _link_function('gluNextContour', None, [POINTER(GLUtesselator), GLenum], None)

# /usr/include/GL/glu.h:306
gluNurbsCallback = _link_function('gluNurbsCallback', None, [POINTER(GLUnurbs), GLenum, _GLUfuncptr], None)

GLvoid = None 	# /usr/include/GL/gl.h:67
# /usr/include/GL/glu.h:307
gluNurbsCallbackData = _link_function('gluNurbsCallbackData', None, [POINTER(GLUnurbs), POINTER(GLvoid)], None)

# /usr/include/GL/glu.h:308
gluNurbsCallbackDataEXT = _link_function('gluNurbsCallbackDataEXT', None, [POINTER(GLUnurbs), POINTER(GLvoid)], None)

# /usr/include/GL/glu.h:309
gluNurbsCurve = _link_function('gluNurbsCurve', None, [POINTER(GLUnurbs), GLint, POINTER(GLfloat), GLint, POINTER(GLfloat), GLint, GLenum], None)

# /usr/include/GL/glu.h:310
gluNurbsProperty = _link_function('gluNurbsProperty', None, [POINTER(GLUnurbs), GLenum, GLfloat], None)

# /usr/include/GL/glu.h:311
gluNurbsSurface = _link_function('gluNurbsSurface', None, [POINTER(GLUnurbs), GLint, POINTER(GLfloat), GLint, POINTER(GLfloat), GLint, GLint, POINTER(GLfloat), GLint, GLint, GLenum], None)

# /usr/include/GL/glu.h:312
gluOrtho2D = _link_function('gluOrtho2D', None, [GLdouble, GLdouble, GLdouble, GLdouble], None)

# /usr/include/GL/glu.h:313
gluPartialDisk = _link_function('gluPartialDisk', None, [POINTER(GLUquadric), GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble], None)

# /usr/include/GL/glu.h:314
gluPerspective = _link_function('gluPerspective', None, [GLdouble, GLdouble, GLdouble, GLdouble], None)

# /usr/include/GL/glu.h:315
gluPickMatrix = _link_function('gluPickMatrix', None, [GLdouble, GLdouble, GLdouble, GLdouble, POINTER(GLint)], None)

# /usr/include/GL/glu.h:316
gluProject = _link_function('gluProject', GLint, [GLdouble, GLdouble, GLdouble, POINTER(GLdouble), POINTER(GLdouble), POINTER(GLint), POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble)], None)

# /usr/include/GL/glu.h:317
gluPwlCurve = _link_function('gluPwlCurve', None, [POINTER(GLUnurbs), GLint, POINTER(GLfloat), GLint, GLenum], None)

# /usr/include/GL/glu.h:318
gluQuadricCallback = _link_function('gluQuadricCallback', None, [POINTER(GLUquadric), GLenum, _GLUfuncptr], None)

# /usr/include/GL/glu.h:319
gluQuadricDrawStyle = _link_function('gluQuadricDrawStyle', None, [POINTER(GLUquadric), GLenum], None)

# /usr/include/GL/glu.h:320
gluQuadricNormals = _link_function('gluQuadricNormals', None, [POINTER(GLUquadric), GLenum], None)

# /usr/include/GL/glu.h:321
gluQuadricOrientation = _link_function('gluQuadricOrientation', None, [POINTER(GLUquadric), GLenum], None)

# /usr/include/GL/glu.h:322
gluQuadricTexture = _link_function('gluQuadricTexture', None, [POINTER(GLUquadric), GLboolean], None)

# /usr/include/GL/glu.h:323
gluScaleImage = _link_function('gluScaleImage', GLint, [GLenum, GLsizei, GLsizei, GLenum, POINTER(None), GLsizei, GLsizei, GLenum, POINTER(GLvoid)], None)

# /usr/include/GL/glu.h:324
gluSphere = _link_function('gluSphere', None, [POINTER(GLUquadric), GLdouble, GLint, GLint], None)

# /usr/include/GL/glu.h:325
gluTessBeginContour = _link_function('gluTessBeginContour', None, [POINTER(GLUtesselator)], None)

# /usr/include/GL/glu.h:326
gluTessBeginPolygon = _link_function('gluTessBeginPolygon', None, [POINTER(GLUtesselator), POINTER(GLvoid)], None)

# /usr/include/GL/glu.h:327
gluTessCallback = _link_function('gluTessCallback', None, [POINTER(GLUtesselator), GLenum, _GLUfuncptr], None)

# /usr/include/GL/glu.h:328
gluTessEndContour = _link_function('gluTessEndContour', None, [POINTER(GLUtesselator)], None)

# /usr/include/GL/glu.h:329
gluTessEndPolygon = _link_function('gluTessEndPolygon', None, [POINTER(GLUtesselator)], None)

# /usr/include/GL/glu.h:330
gluTessNormal = _link_function('gluTessNormal', None, [POINTER(GLUtesselator), GLdouble, GLdouble, GLdouble], None)

# /usr/include/GL/glu.h:331
gluTessProperty = _link_function('gluTessProperty', None, [POINTER(GLUtesselator), GLenum, GLdouble], None)

# /usr/include/GL/glu.h:332
gluTessVertex = _link_function('gluTessVertex', None, [POINTER(GLUtesselator), POINTER(GLdouble), POINTER(GLvoid)], None)

# /usr/include/GL/glu.h:333
gluUnProject = _link_function('gluUnProject', GLint, [GLdouble, GLdouble, GLdouble, POINTER(GLdouble), POINTER(GLdouble), POINTER(GLint), POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble)], None)

# /usr/include/GL/glu.h:334
gluUnProject4 = _link_function('gluUnProject4', GLint, [GLdouble, GLdouble, GLdouble, GLdouble, POINTER(GLdouble), POINTER(GLdouble), POINTER(GLint), GLdouble, GLdouble, POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble)], None)


__all__ = ['GLU_EXT_object_space_tess', 'GLU_EXT_nurbs_tessellator',
'GLU_FALSE', 'GLU_TRUE', 'GLU_VERSION_1_1', 'GLU_VERSION_1_2',
'GLU_VERSION_1_3', 'GLU_VERSION', 'GLU_EXTENSIONS', 'GLU_INVALID_ENUM',
'GLU_INVALID_VALUE', 'GLU_OUT_OF_MEMORY', 'GLU_INCOMPATIBLE_GL_VERSION',
'GLU_INVALID_OPERATION', 'GLU_OUTLINE_POLYGON', 'GLU_OUTLINE_PATCH',
'GLU_NURBS_ERROR', 'GLU_ERROR', 'GLU_NURBS_BEGIN', 'GLU_NURBS_BEGIN_EXT',
'GLU_NURBS_VERTEX', 'GLU_NURBS_VERTEX_EXT', 'GLU_NURBS_NORMAL',
'GLU_NURBS_NORMAL_EXT', 'GLU_NURBS_COLOR', 'GLU_NURBS_COLOR_EXT',
'GLU_NURBS_TEXTURE_COORD', 'GLU_NURBS_TEX_COORD_EXT', 'GLU_NURBS_END',
'GLU_NURBS_END_EXT', 'GLU_NURBS_BEGIN_DATA', 'GLU_NURBS_BEGIN_DATA_EXT',
'GLU_NURBS_VERTEX_DATA', 'GLU_NURBS_VERTEX_DATA_EXT', 'GLU_NURBS_NORMAL_DATA',
'GLU_NURBS_NORMAL_DATA_EXT', 'GLU_NURBS_COLOR_DATA',
'GLU_NURBS_COLOR_DATA_EXT', 'GLU_NURBS_TEXTURE_COORD_DATA',
'GLU_NURBS_TEX_COORD_DATA_EXT', 'GLU_NURBS_END_DATA',
'GLU_NURBS_END_DATA_EXT', 'GLU_NURBS_ERROR1', 'GLU_NURBS_ERROR2',
'GLU_NURBS_ERROR3', 'GLU_NURBS_ERROR4', 'GLU_NURBS_ERROR5',
'GLU_NURBS_ERROR6', 'GLU_NURBS_ERROR7', 'GLU_NURBS_ERROR8',
'GLU_NURBS_ERROR9', 'GLU_NURBS_ERROR10', 'GLU_NURBS_ERROR11',
'GLU_NURBS_ERROR12', 'GLU_NURBS_ERROR13', 'GLU_NURBS_ERROR14',
'GLU_NURBS_ERROR15', 'GLU_NURBS_ERROR16', 'GLU_NURBS_ERROR17',
'GLU_NURBS_ERROR18', 'GLU_NURBS_ERROR19', 'GLU_NURBS_ERROR20',
'GLU_NURBS_ERROR21', 'GLU_NURBS_ERROR22', 'GLU_NURBS_ERROR23',
'GLU_NURBS_ERROR24', 'GLU_NURBS_ERROR25', 'GLU_NURBS_ERROR26',
'GLU_NURBS_ERROR27', 'GLU_NURBS_ERROR28', 'GLU_NURBS_ERROR29',
'GLU_NURBS_ERROR30', 'GLU_NURBS_ERROR31', 'GLU_NURBS_ERROR32',
'GLU_NURBS_ERROR33', 'GLU_NURBS_ERROR34', 'GLU_NURBS_ERROR35',
'GLU_NURBS_ERROR36', 'GLU_NURBS_ERROR37', 'GLU_AUTO_LOAD_MATRIX',
'GLU_CULLING', 'GLU_SAMPLING_TOLERANCE', 'GLU_DISPLAY_MODE',
'GLU_PARAMETRIC_TOLERANCE', 'GLU_SAMPLING_METHOD', 'GLU_U_STEP', 'GLU_V_STEP',
'GLU_NURBS_MODE', 'GLU_NURBS_MODE_EXT', 'GLU_NURBS_TESSELLATOR',
'GLU_NURBS_TESSELLATOR_EXT', 'GLU_NURBS_RENDERER', 'GLU_NURBS_RENDERER_EXT',
'GLU_OBJECT_PARAMETRIC_ERROR', 'GLU_OBJECT_PARAMETRIC_ERROR_EXT',
'GLU_OBJECT_PATH_LENGTH', 'GLU_OBJECT_PATH_LENGTH_EXT', 'GLU_PATH_LENGTH',
'GLU_PARAMETRIC_ERROR', 'GLU_DOMAIN_DISTANCE', 'GLU_MAP1_TRIM_2',
'GLU_MAP1_TRIM_3', 'GLU_POINT', 'GLU_LINE', 'GLU_FILL', 'GLU_SILHOUETTE',
'GLU_SMOOTH', 'GLU_FLAT', 'GLU_NONE', 'GLU_OUTSIDE', 'GLU_INSIDE',
'GLU_TESS_BEGIN', 'GLU_BEGIN', 'GLU_TESS_VERTEX', 'GLU_VERTEX',
'GLU_TESS_END', 'GLU_END', 'GLU_TESS_ERROR', 'GLU_TESS_EDGE_FLAG',
'GLU_EDGE_FLAG', 'GLU_TESS_COMBINE', 'GLU_TESS_BEGIN_DATA',
'GLU_TESS_VERTEX_DATA', 'GLU_TESS_END_DATA', 'GLU_TESS_ERROR_DATA',
'GLU_TESS_EDGE_FLAG_DATA', 'GLU_TESS_COMBINE_DATA', 'GLU_CW', 'GLU_CCW',
'GLU_INTERIOR', 'GLU_EXTERIOR', 'GLU_UNKNOWN', 'GLU_TESS_WINDING_RULE',
'GLU_TESS_BOUNDARY_ONLY', 'GLU_TESS_TOLERANCE', 'GLU_TESS_ERROR1',
'GLU_TESS_ERROR2', 'GLU_TESS_ERROR3', 'GLU_TESS_ERROR4', 'GLU_TESS_ERROR5',
'GLU_TESS_ERROR6', 'GLU_TESS_ERROR7', 'GLU_TESS_ERROR8',
'GLU_TESS_MISSING_BEGIN_POLYGON', 'GLU_TESS_MISSING_BEGIN_CONTOUR',
'GLU_TESS_MISSING_END_POLYGON', 'GLU_TESS_MISSING_END_CONTOUR',
'GLU_TESS_COORD_TOO_LARGE', 'GLU_TESS_NEED_COMBINE_CALLBACK',
'GLU_TESS_WINDING_ODD', 'GLU_TESS_WINDING_NONZERO',
'GLU_TESS_WINDING_POSITIVE', 'GLU_TESS_WINDING_NEGATIVE',
'GLU_TESS_WINDING_ABS_GEQ_TWO', 'GLUnurbs', 'GLUquadric', 'GLUtesselator',
'GLUnurbsObj', 'GLUquadricObj', 'GLUtesselatorObj', 'GLUtriangulatorObj',
'GLU_TESS_MAX_COORD', '_GLUfuncptr', 'gluBeginCurve', 'gluBeginPolygon',
'gluBeginSurface', 'gluBeginTrim', 'gluBuild1DMipmapLevels',
'gluBuild1DMipmaps', 'gluBuild2DMipmapLevels', 'gluBuild2DMipmaps',
'gluBuild3DMipmapLevels', 'gluBuild3DMipmaps', 'gluCheckExtension',
'gluCylinder', 'gluDeleteNurbsRenderer', 'gluDeleteQuadric', 'gluDeleteTess',
'gluDisk', 'gluEndCurve', 'gluEndPolygon', 'gluEndSurface', 'gluEndTrim',
'gluErrorString', 'gluGetNurbsProperty', 'gluGetString', 'gluGetTessProperty',
'gluLoadSamplingMatrices', 'gluLookAt', 'gluNewNurbsRenderer',
'gluNewQuadric', 'gluNewTess', 'gluNextContour', 'gluNurbsCallback',
'gluNurbsCallbackData', 'gluNurbsCallbackDataEXT', 'gluNurbsCurve',
'gluNurbsProperty', 'gluNurbsSurface', 'gluOrtho2D', 'gluPartialDisk',
'gluPerspective', 'gluPickMatrix', 'gluProject', 'gluPwlCurve',
'gluQuadricCallback', 'gluQuadricDrawStyle', 'gluQuadricNormals',
'gluQuadricOrientation', 'gluQuadricTexture', 'gluScaleImage', 'gluSphere',
'gluTessBeginContour', 'gluTessBeginPolygon', 'gluTessCallback',
'gluTessEndContour', 'gluTessEndPolygon', 'gluTessNormal', 'gluTessProperty',
'gluTessVertex', 'gluUnProject', 'gluUnProject4']
# END GENERATED CONTENT (do not edit above this line)


