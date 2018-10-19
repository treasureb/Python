#! /usr/bin/env
#coding=utf-8

n = int(input("Enter the number of students:"))#学生人数
data = {} #用来存储数据的字典变量
Subjects = ('Physics','Maths','History')#元组保存所有的科目
for i in range(0,n):
    name = input('Enter the name of the student{}:'.format(i+1))#获得学生名称
    marks = []
    for x in Subjects:
        marks.append(int(input('Enter marks of {}:'.format(x))))#获得每一科的分数
        data[name] = marks

for x,y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x,total))
    if total < 120:
        print(x,"failed:(")
    else:
        print(x,"passed:)")
