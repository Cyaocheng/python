#!/usr/bin/python
#-*- coding: UTF-8 -*- 

class People(object):

     def __init__(self,Salary="",House=""):
         self.Salary = Salary
         self.House = House

     def house_where(self):

         if self.Salary >= 20000:
            self.House = "可以租住2～3环之间"
            return self.House

         elif 15000 <= self.Salary < 20000:
            self.House = "可以租住4～5环之间"
            return self.House

         elif 10000 <= self.Salary < 15000:
            self.House = "可以租住4～5环之间"
            return self.House

         elif self.Salary < 10000:
            self.House = "可以租住5环之外"
            return self.House

ItWorker = People(20000)
print ItWorker.house_where()
