#define PY_SSIZE_T_CLEAN

#include <Python.h>

#include "include/yammpy.h"

/* yammpy_func is used to wrap a libm function f that takes a double argument and returns a double. */

static PyObject *
yammpy_func(PyObject* args, double (*func)(double)) {
    double x, ret;

    x = PyFloat_AsDouble(args);

    if (x == -1.0 && PyErr_Occurred())
        return NULL;

    ret = (*func)(x);

    if (Py_IS_NAN(ret) && !Py_IS_NAN(x)) {
        PyErr_SetString(PyExc_ValueError, "domain error"); /* invalid arg */
        return NULL;
    }
    
    return PyFloat_FromDouble(ret);
}

static PyMethodDef yammpy_methods[] = {
    {"acos",            yammpy_acos,      METH_O,         yammpy_acos_doc},
    {"acosh",           yammpy_acosh,     METH_O,         yammpy_acosh_doc},
    {"asin",            yammpy_asin,      METH_O,         yammpy_asin_doc},
    {"asinh",           yammpy_asinh,     METH_O,         yammpy_asinh_doc},
    {"atan",            yammpy_atan,      METH_O,         yammpy_atan_doc},
    {"atanh",           yammpy_atanh,     METH_O,         yammpy_atanh_doc},
    {"cos",             yammpy_cos,       METH_O,         yammpy_cos_doc},
    {"cosh",            yammpy_cosh,      METH_O,         yammpy_cosh_doc},
    {"erf",             yammpy_erf,       METH_O,         yammpy_erf_doc},
    {"erfc",            yammpy_erfc,      METH_O,         yammpy_erfc_doc},
    {"exp",             yammpy_exp,       METH_O,         yammpy_exp_doc},
    {"expm1",           yammpy_expm1,     METH_O,         yammpy_expm1_doc},
	{"fabs",            yammpy_fabs,      METH_O,         yammpy_fabs_doc},
    {"gamma",           yammpy_gamma,     METH_O,         yammpy_gamma_doc},
    {"lgamma",          yammpy_lgamma,    METH_O,         yammpy_lgamma_doc},
    {"log1p",           yammpy_log1p,     METH_O,         yammpy_log1p_doc},
    {"sin",             yammpy_sin,       METH_O,         yammpy_sin_doc},
    {"sinh",            yammpy_sinh,      METH_O,         yammpy_sinh_doc},
    {"sqrt",            yammpy_sqrt,      METH_O,         yammpy_sqrt_doc},
    {"tan",             yammpy_tan,       METH_O,         yammpy_tan_doc},
    {"tanh",            yammpy_tanh,      METH_O,         yammpy_tanh_doc},
    {NULL}, /* sentinel */
};

PyDoc_STRVAR(yammpy_doc, "yammpy provides access to the mathematical functions");

static struct PyModuleDef yammpy = {
    PyModuleDef_HEAD_INIT,
    "yammpy",
    yammpy_doc,
    -1,
    yammpy_methods,
};

PyMODINIT_FUNC
PyInit_yammpy(void) {
	PyObject *yamm;

	yamm = PyModule_Create(&yammpy);

	if(yamm == NULL)
		return NULL;
	
	PyModule_AddObject(yamm, "pi", PyFloat_FromDouble(PI));
    PyModule_AddObject(yamm, "e", PyFloat_FromDouble(E));
    PyModule_AddObject(yamm, "tau", PyFloat_FromDouble(TAU));
	PyModule_AddObject(yamm, "phi", PyFloat_FromDouble(PHI));
    PyModule_AddObject(yamm, "wal", PyFloat_FromDouble(WAL));
	PyModule_AddObject(yamm, "inf", PyFloat_FromDouble(INFINITY));
    PyModule_AddObject(yamm, "nan", PyFloat_FromDouble(NAN));

    return yamm;
}
