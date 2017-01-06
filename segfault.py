import cytest


def init():
    "instantiate a tuple and stores its pointer inside cytest module"
    a_tuple = (1, 2, 3)
    # at this point a_tuple is still live and its pointer is valid
    cytest.set_pointer(a_tuple)
    # now a_tuple gets out of context and is garbage collected

# at this point the object pointed by cytest module is collected and
# accessing it generates a segfault
print(cytest.get_pointer())
