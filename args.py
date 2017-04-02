#!/usr/bin/python
#-*- coding: UTF-8 -*-

import random,string
import string

def all_the_args(*args, **kwargs):
    print args
    print kwargs
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""
 
# When calling functions, you can do the opposite of varargs/kwargs!
# Use * to expand tuples and use ** to expand kwargs.
# 在调用函数时，定位参数和关键字参数还可以反过来用。
# 使用 * 来展开元组，使用 ** 来展开关键字参数。
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args) # equivalent to foo(1, 2, 3, 4)
                    # 相当于 all_the_args(1, 2, 3, 4)
all_the_args(**kwargs) # equivalent to foo(a=3, b=4)
                       # 相当于 all_the_args(a=3, b=4)
all_the_args(*args, **kwargs) # equivalent to foo(1, 2, 3, 4, a=3, b=4)
                              # 相当于 all_the_args(1, 2, 3, 4, a=3, b=4)
