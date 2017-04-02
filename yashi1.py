#! /usr/bin/python
#coding:utf-8


list1 = [2,3,4,88,33223,"3323", ["list", "中国"]]
print list1

list1.insert(0,"fjdkja");

for item in list1:
    print item


list1.remove("fjdkja");

print list1 
#for item in list1:
#     print item

list1.pop(0);
print list1


print "#####" 
print sorted(list1,reverse=True);
print "#####" 
print list1

print "----------" 
list1.sort();
print list1 
print "----------" 

list1.reverse();
print list1 

