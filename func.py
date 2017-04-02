#!/usr/bin/python
#-*- coding: UTF-8 -*-

import random,string
import string

suit= [1,2,3,4,5]


def chg_lis(suit):

    for i in xrange(len(suit)-1 ):
         suit[i] += 10 

    return  suit

print( chg_lis(suit))

print suit
