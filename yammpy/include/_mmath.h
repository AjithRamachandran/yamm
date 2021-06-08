#ifndef _MMATH_H
#define _MMATH_H

/****************************************
<math.h> functions with added inspections
*****************************************/

PyDoc_STRVAR(_mmath_fmod_doc, "Returns the floating-point remainder of the division x/y.");

#define _MMATH_FMOD_METHODDEF   \
    {"fmod", (PyCFunction)_mmath_fmod, METH_VARARGS, _mmath_fmod_doc},

PyDoc_STRVAR(_mmath_remainder_doc, "Returns the signed remainder of the division x/y.");

#define _MMATH_REMAINDER_METHODDEF   \
    {"remainder", (PyCFunction)_mmath_remainder, METH_VARARGS, _mmath_remainder_doc},

PyDoc_STRVAR(_mmath_sqrt_doc, "Returns square root of x.");

#define _MMATH_SQRT_METHODDEF   \
    {"sqrt", (PyCFunction)_mmath_sqrt, METH_O, _mmath_sqrt_doc},

#endif // _MMATH_H
