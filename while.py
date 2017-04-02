#!/usr/bin/python
#-*- coding: UTF-8 -*-

#i = 0

#while True:
#     i += 1
#     print i,
#     if i > 9:
#         print "\n"
#         break

#i = 0
#while i < 10:
#      i += 1
#      print i,
#print "\n"

import random,string

number = random.randint(0,100)

print("猜数字游戏，数字0-100\n")

while True:

     guess=raw_input("请输入数字\n")

     if guess.isdigit():

         guess = int(guess)

         if guess == number:
             print("猜对了\n"),guess
             break
         elif guess > number:
             print("猜的数字太大了\n"),guess
         else :
             print("猜的数字太小了\n"),guess

     else:
         print("请重新输入数字\n")
