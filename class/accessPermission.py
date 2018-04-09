# -*- coding: utf-8 -*-
#类的权限

#1._name ->表示在子类中可以被访问
#2.__name ->表示该变量是一个私有成员，外部不能访问

class Person(object):
    def __init__(self,name,score):
        self.name = name
        self.__score = score

p = Person('Bob',59)

print p.name
try:
    print p.__socre
except:
    print 'AttributeError'
