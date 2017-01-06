import cytest


class A:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return "this is the content of A: {}".format(self.args)

a = A(1, 2, 3)
cytest.set_pointer(a)
# at this point a is still referenced so printing it and
# printing the result of ctyest.get_pointer() gives the same result
print(a)
print(cytest.get_pointer())

# here a is assigned a new object so the previous one is collected by
# the garbage collector but allocating a new object seems to recycle
# the released memory pointed by cytest internal pointer so printing
# the result of cytest.get_pointer() gives the content of b; this
# behaviour almost drove me crazy while debugging a wrapper I was developing
# around wakaama LWM2M library
a = A(4, 5, 6)
b = A(7, 8, 9)
print(a)
print(cytest.get_pointer())
