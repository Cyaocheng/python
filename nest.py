#!/usr/bin/python
#-*- coding: UTF-8 -*- 

def outer(func):

    def inner():
        #print y
        func()
    return inner

@outer
def foo():
    print "in foo "
    #print y

#p = (outer(5))(6)

#p = outer(foo)(6)

print id(foo)
#foo = outer(foo)(88)
foo = foo()
print id(foo)
