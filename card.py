#!/usr/bin/python
#-*- coding: UTF-8 -*-

import random,string
import string

dict_source = {
               "A":  "Ace", 
               "2":  "2", 
               "3":  "3", 
               "4":  "4", 
               "5":  "5", 
               "6":  "6", 
               "7":  "7", 
               "8":  "8", 
               "9":  "9", 
               "T":  "10", 
               "J":  "Jack", 
               "Q":  "Queen", 
               "K":  "King" 
               }
dict_suit = {
               "D": "Diamonds",
               "C": "Clubs",
               "H": "Hearts",
               "S": "Spades"
             }

input1=['A','2','3','4','5','6','7','8','9', 'T','J','Q','K']
input2=['D','C','H','S']

value = ['Ace','2','3','4','5','6','7','8','9', '10','Jack','Queen','King']
suit= ['Diamonds','Clubs','Hearts','Spades']


def card_namer_dict(str1,str2):
    if str1 in dict_source.keys() and str2 in dict_suit.keys():
         x1 = dict_source[str1]
         x2 = dict_suit[str2]
         return x1 + '  of  '+ x2

    else :
         return 'CHEATER'

def card_namer(str1,str2):
    if str1 in input1 and str2 in input2:
         x1 = input1.index(str1)
         x2 = input2.index(str2)
         return value[x1] + '  of  '+ suit[x2]

    else :
         return 'CHEATER'

#str1 = card_namer('A','D' )
#str1 = card_namer('A','K' )
#print str1

x = raw_input("please input name:\n").strip()
y = raw_input("please input suit:\n").strip()

print( card_namer(x,y))
print( card_namer_dict(x,y))


