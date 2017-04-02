#! /usr/bin/python
#coding:utf-8

file1 = open("source.txt","r")
file2 = open("des.txt","w")

while True:
    line = file1.readline()

    s1 = line.find("****")
    s2 = line.find("公司性质")
    s3 = line.find("公司规模")
    s4 = line.find("公司地址")
    s5 = line.find("公司行业")
    s6 = line.find("公司网址")
    s7 = line.find("公司介绍")

    if s1 > 0:
         file2.write(line)
         line = file1.readline()
         line = file1.readline()
         file2.write("公司名称:"+line)

    if s2 >= 0:
         file2.write(line[:s3]+'\n')
         file2.write(line[s3:s4]+'\n')
         file2.write(line[s4:s5]+'\n')
         file2.write(line[s5:s6]+'\n')
         file2.write(line[s6:]+'\n')
         mylist=[]
         while True:
             line = file1.readline()
             s8 = line.find("****")
             if s8 < 0:
                 mylist.append(line)

             if s8 > 0:
                 file2.write(":".join(mylist)+'\n')
                 file2.write(line)
                 line = file1.readline()
                 line = file1.readline()
                 file2.write("公司名称:"+line)

                 break
             if not line:
                 file2.write(":".join(mylist)+'\n')

                 break
    if not line:
    
        break

file1.close();
file2.close();

