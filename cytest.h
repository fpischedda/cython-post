/* Generated by Cython 0.25.2 */

#ifndef __PYX_HAVE__cytest
#define __PYX_HAVE__cytest


#ifndef __PYX_HAVE_API__cytest

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#ifndef DL_IMPORT
  #define DL_IMPORT(_T) _T
#endif

__PYX_EXTERN_C DL_IMPORT(void) _set_pointer(void *);
__PYX_EXTERN_C DL_IMPORT(PyObject) *get_pointer(int __pyx_skip_dispatch);
__PYX_EXTERN_C DL_IMPORT(void) set_pointer(PyObject *, int __pyx_skip_dispatch);

#endif /* !__PYX_HAVE_API__cytest */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initcytest(void);
#else
PyMODINIT_FUNC PyInit_cytest(void);
#endif

#endif /* !__PYX_HAVE__cytest */
