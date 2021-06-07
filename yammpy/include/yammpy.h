#ifndef YAMMPY_H
#define YAMMPY_H

#include <Python.h>

/* constants */

#ifndef PI
#define PI 3.1415926535897932384626433832795029L
#endif

#ifndef E
#define E 2.7182818284590452353602874713526625L
#endif

#ifndef TAU
#define TAU 6.2831853071795864769252867665590057683943L
#endif

#ifndef PHI
#define PHI 1.61803398874989484820L
#endif

#ifndef WAL
#define WAL 2.09455148154232659148L
#endif

/*
function wrapper for <math.h> functions
*/

static PyObject* yammpy_func(PyObject* , double (*)(double));

#define FUNC(funcname, func, docstring)                                     \
    static PyObject* yammpy_##funcname(PyObject* self, PyObject* args) {    \
        return yammpy_func(args, func);                                     \
    }                                                                       \
    PyDoc_STRVAR(yammpy_##funcname##_doc, docstring);


/*
wrap functions from <math.h> library 
*/

FUNC(acos, acos, "Returns the arc cosine of x (arccos(x)) in the range [0 ; π].")
FUNC(acosh, acosh, "Returns the inverse hyperbolic cosine of arg (cosh^-1(arg), or arcosh(arg)) on the interval [0, +∞].")
FUNC(asin, asin, "Returns the arc sine of x (arcsin(x)) in the range [-(π/2) ; +(π/2).")
FUNC(asinh, asinh, "Returns the inverse hyperbolic sine of arg (sinh^-1(arg), or arsinh(arg).")
FUNC(atan, atan, "Returns the arc tangent of x (arctan(x)) in the range [-(π/2) ; +(π/2)].")
FUNC(atanh, atanh, "Returns the inverse hyperbolic tangent of arg (tanh^-1(arg), or artanh(arg)).")
FUNC(cos, cos, "Returns the sine of x (cos(x)) in the range [-1 ; +1].")
FUNC(cosh, cosh, "Returns the hyperbolic cosine of arg (cosh(arg), or (((e^arg)+(e^-arg))/2).")
FUNC(erf, erf, "Returns value of the error function of x.")
FUNC(erfc, erfc, "Returns value of the complementary error function of x.")
FUNC(exp, exp, "Returns  the base-e exponential of arg (e^arg).")
FUNC(expm1, expm1, "Returns e^arg-1.")
FUNC(fabs, fabs, "Returns the absolute value of floating point value x.")
FUNC(gamma, tgamma, "Returns the value of the gamma function of x.")
FUNC(lgamma, lgamma, "Returns the value of the logarithm of the gamma function of x.")
FUNC(log1p, log1p, "Returns ln(1+arg)")
FUNC(sin, sin, "Returns the sine of x (sin(x)) in the range [-1 ; +1].")
FUNC(sinh, sinh, "Returns the hyperbolic sine of x (sinh(x), or (((e^arg)-(e^-arg))/2)")
FUNC(sqrt, sqrt, "Returns square root of x.")
FUNC(tan, tan, "Returns the sine of x (tan(x)).")
FUNC(tanh, tanh, "Returns the hyperbolic tangent of arg (tanh(arg), or (((e^arg)-(e^-arg))/((e^arg)+(e^-arg)))")

#endif // YAMMPY_H
