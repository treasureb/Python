# -*- coding: utf-8 -*-
#定义类方法
#方法分为实例方法和类方法

#class定义的全部是实例方法，实例方法第一个参数self是实例本身

#定义类方法
class Person(object):
    __count = 0
    #通过标记@classmethod,该方法将绑定到Person类
    #类方法的第一个参数将传入类本身，通常参数名为cls
    #cls.__count实际上相当于Person.__count
    @classmethod
    def how_many(cls):
        return cls.__count
    def __init__(self,name):
        self.name = name
        Person.__count = Person.__count+1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()
