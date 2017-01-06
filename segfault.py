import cytest

def init():
    a_tuple = (1, 2, 3)
    cytest.set_pointer(a_tuple)
print(cytest.get_pointer())
