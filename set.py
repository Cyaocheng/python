#!/usr/bin/python
#-*- coding: UTF-8 -*-

import random,string
import string

filled_set = {1, 2, 2, 3, 4}
other_set = {2, 3, 4, 5, 6}

print filled_set & other_set
print filled_set | other_set
print filled_set - other_set
print 1 in other_set

try:
   print 1 in other_set
   raise IndexError("This is an index error")
except IndexError as e:
   pass
