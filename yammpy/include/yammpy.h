#ifndef YAMMPY_H
#define YAMMPY_H

/******************************************
new functions implemented for yammpy module
*******************************************/

PyDoc_STRVAR(yammpy_degrees_doc, "Converts angle x radians to degrees");

#define YAMMPY_DEGREES_METHODDEF  \
    {"degrees", (PyCFunction)yammpy_degree, METH_O, yammpy_degrees_doc},

PyDoc_STRVAR(yammpy_radians_doc, "Converts angle x radians to degrees");

#define YAMMPY_RADIANS_METHODDEF  \
    {"radians", (PyCFunction)yammpy_radian, METH_O, yammpy_radians_doc},

PyDoc_STRVAR(yammpy_lcm_doc, "Returns the lcm of numbers in an array.");

#define YAMMPY_LCM_METHODDEF   \
    {"lcm", (PyCFunction)yammpy_lcm, METH_O, yammpy_lcm_doc},

PyDoc_STRVAR(yammpy_gcd_doc, "Returns the gcd of numbers in an array.");

#define YAMMPY_GCD_METHODDEF   \
    {"gcd", (PyCFunction)yammpy_gcd, METH_O, yammpy_gcd_doc},

PyDoc_STRVAR(yammpy_ncr_doc, "Returns the ncr of x.");

#define YAMMPY_NCR_METHODDEF   \
    {"ncr", (PyCFunction)yammpy_ncr, METH_O, yammpy_ncr_doc},

PyDoc_STRVAR(yammpy_isfinite_doc, "Returns if x is finite or not.");

#define YAMMPY_ISFINITE_METHODDEF  \
    {"isfinite", (PyCFunction)yammpy_isfinite, METH_O, yammpy_isfinite_doc},

PyDoc_STRVAR(yammpy_isinf_doc, "Returns if x is infinity or not.");

#define YAMMPY_ISINF_METHODDEF  \
    {"isinf", (PyCFunction)yammpy_isinf, METH_O, yammpy_isinf_doc},

PyDoc_STRVAR(yammpy_isnan_doc, "Returns if x is NaN.");

#define YAMMPY_ISNAN_METHODDEF  \
    {"isnan", (PyCFunction)yammpy_isnan, METH_O, yammpy_isnan_doc},

PyDoc_STRVAR(yammpy_isperfsqr_doc, "Returns if x is NaN.");

#define YAMMPY_ISPERFSQR_METHODDEF  \
    {"isperfsqr", (PyCFunction)yammpy_isperfsqr, METH_O, yammpy_isperfsqr_doc},

PyDoc_STRVAR(yammpy_sum_doc, "Returns sum of values of array.");

#define YAMMPY_SUM_METHODDEF  \
    {"sum", (PyCFunction)yammpy_sum, METH_O, yammpy_sum_doc},

PyDoc_STRVAR(yammpy_prod_doc, "Returns product of values of array.");

#define YAMMPY_PROD_METHODDEF  \
    {"prod", (PyCFunction)yammpy_prod, METH_O, yammpy_prod_doc},

PyDoc_STRVAR(yammpy_factorial_doc, "Returns factorial of x.");

#define YAMMPY_FACTORIAL_METHODDEF  \
    {"factorial", (PyCFunction)yammpy_factorial, METH_O, yammpy_factorial_doc},

#endif // YAMMPY_H
