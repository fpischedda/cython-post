cdef void* POINTER

cdef public void _set_pointer(void *p):
    global POINTER
    POINTER = p

cpdef public object get_pointer():
    return <object>POINTER

cpdef public void set_pointer(obj):
    _set_pointer(<void*>obj)
