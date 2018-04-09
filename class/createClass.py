# -*- coding: utf-8 -*-

#创建一个空类
class Person(object):
    pass

#创建两个实例
guodong = Person()
yiming = Person()

#python是动态语言，可以动态添加属性
guodong.name = 'XiaoGuoDong'
guodong.gender = 'Male'
guodong.birth = '1996-9-16'

yiming.birth = '1997-6-6'
yiming.gender = 'Famale'
yiming.grade = 2

#实例的属性可以像普通变量一样进行操作
yiming.grade = yiming.grade+1
print yiming.grade

#------------------------------------------------
#练习
class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1,p2,p3]
L2 = sorted(L1,key=lambda x:x.name)

print L2[0].name
print L2[1].name
print L2[2].name
