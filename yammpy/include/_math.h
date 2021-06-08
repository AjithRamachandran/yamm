#ifndef _MATH_H
#define _MATH_H

/****************************
 untouched <math.h> functions 
*****************************/

/* yammpy_func_arg is used to wrap a libm function f that takes a double argument and returns a double. */

static PyObject *
_math_func_arg(PyObject* arg, double (*func)(double)) {
    double x, ret;

    x = PyFloat_AsDouble(arg);

    if (x == -1.0 && PyErr_Occurred())
        return NULL;

    ret = (*func)(x);

    if (Py_IS_NAN(ret) && !Py_IS_NAN(x)) {
        PyErr_SetString(PyExc_ValueError, "domain error"); /* invalid arg */
        return NULL;
    }
    
    return PyFloat_FromDouble(ret);
}

/* yammpy_func_args is used to wrap a libm function f that takes two double arguments and returns a double. */

static PyObject *
_math_func_args(PyObject *args, double (*func)(double, double)) {
    double x, y, ret;

    if (!PyArg_ParseTuple(args, "dd", &x, &y))
        return NULL;

    if (PyErr_Occurred())
        return NULL;

    ret = (*func)(x, y);

    if (Py_IS_NAN(ret)) {
        if(!Py_IS_NAN(x) || !Py_IS_NAN(y)) {
            PyErr_SetString(PyExc_ValueError, "NaN values are not accepted."); /* invalid arg */
            return NULL;
        }
    }
    
    return PyFloat_FromDouble(ret);
}

/* function wrapper for <math.h> functions */

#define FUNC(funcname, func, docstring)                                     \
    static PyObject* _math_##funcname(PyObject* self, PyObject* args) {    \
        return _math_func_arg(args, func);                                     \
    }                                                                       \
    PyDoc_STRVAR(_math_##funcname##_doc, docstring);

#define FUNC2(funcname, func, docstring)                                     \
    static PyObject* _math_##funcname(PyObject* self, PyObject* args) {    \
        return _math_func_args(args, func);                                     \
    }                                                                       \
    PyDoc_STRVAR(_math_##funcname##_doc, docstring);

/* wrap functions from <math.h> library  */

FUNC(acos, acos, "Returns the arc cosine of x (arccos(x)) in the range [0 ; π].")
FUNC(acosh, acosh, "Returns the inverse hyperbolic cosine of x (cosh^-1(x), or arcosh(x)) on the interval [0, +∞].")
FUNC(asin, asin, "Returns the arc sine of x (arcsin(x)) in the range [-(π/2) ; +(π/2).")
FUNC(asinh, asinh, "Returns the inverse hyperbolic sine of x (sinh^-1(x), or arsinh(x).")
FUNC(atan, atan, "Returns the arc tangent of x (arctan(x)) in the range [-(π/2) ; +(π/2)].")
FUNC(atanh, atanh, "Returns the inverse hyperbolic tangent of x (tanh^-1(x), or artanh(x)).")
FUNC(cbrt, cbrt, "Returns cube root of x.")
FUNC(ceil, ceil, "Computes the smallest integer value not less than x.")
FUNC(cos, cos, "Returns the sine of x (cos(x)) in the range [-1 ; +1].")
FUNC(cosh, cosh, "Returns the hyperbolic cosine of x (cosh(x), or (((e^x)+(e^-x))/2).")
FUNC(erf, erf, "Returns value of the error function of x.")
FUNC(erfc, erfc, "Returns value of the complementary error function of x.")
FUNC(exp, exp, "Returns  the base-e exponential of x (e^x).")
FUNC(exp2, exp2, "Returns 2 raised to the x.")
FUNC(expm1, expm1, "Returns e^x-1.")
FUNC(fabs, fabs, "Returns the absolute value of floating point value x.")
FUNC(floor, floor, "Computes the largest integer value not greater than x.")
FUNC(gamma, tgamma, "Returns the value of the gamma function of x.")
FUNC(lgamma, lgamma, "Returns the value of the logarithm of the gamma function of x.")
FUNC(log, log, "Computes natural logarithm (to base e).")
FUNC(log2, log2, "Computes binary logarithm (to base 2).")
FUNC(log10, log10, "Computes common logarithm (to base 10).")
FUNC(log1p, log1p, "Returns ln(1+x)")
FUNC(logb, logb, "Returns the unbiased exponent of x.")
FUNC(nearbyint, nearbyint, "Returns the nearest integer value to x.")
FUNC(sin, sin, "Returns the sine of x (sin(x)) in the range [-1 ; +1].")
FUNC(sinh, sinh, "Returns the hyperbolic sine of x (sinh(x), or (((e^x)-(e^-x))/2)")
FUNC(tan, tan, "Returns the sine of x (tan(x)).")
FUNC(tanh, tanh, "Returns the hyperbolic tangent of x (tanh(x), or (((e^x)-(e^-x))/((e^x)+(e^-x)))")
FUNC(trunc, trunc, "Computes the nearest integer not greater in magnitude than x.")
FUNC2(atan2, atan2, "Returns the arc tangent of y/x in the range [-π ; +π] radians.")
FUNC2(copysign, copysign, "Returns the floating point value with the magnitude of x and the sign of y.")
FUNC2(fdim, fdim, "Returns the positive difference between x and y.")
FUNC2(hypot, hypot, "Returns the hypotenuse of a right-angled triangle, √(x^2 + y^2).")
FUNC2(pow, pow, "Returns x raised to the power of y (x^y).")

#endif // _MATH_H
