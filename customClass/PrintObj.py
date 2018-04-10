# -*- coding: utf-8 -*-

#__str__()函数->将一个类的实例编程str

class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return 'Perosn:%s,%s' % (self.name,self.gender)
    __repr__ = __str__

p = Person('Bob','Male')
print p

#两者的区别
#__str__是显示给用户
#__repr__是显示给开发人员
