# the global pointer
cdef void* POINTER

# a "c" function that stores a pointer in the global variable
cdef public void _set_pointer(void *p):
    global POINTER
    POINTER = p

# returns the python object pointed to by global POINTER
cpdef public object get_pointer():
    return <object>POINTER

# wrapper of the "c" function callable from python
cpdef public void set_pointer(obj):
    _set_pointer(<void*>obj)
