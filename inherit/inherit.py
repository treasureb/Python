# -*- coding: utf-8 -*-

#基类
class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

#派生类
class Student(Person):
    def __init__(self,name,gender,score):
        #使用super(Student,self)初始化基类对象
        super(Student,self).__init__(name,gender)
        self.score = score
    #自己测试
    def Print():
        print self.name
        print self.gender
        print self.score

#函数super(Student,self)将返回当前类继承的基类，即Person
#然后调用__init__()方法,第一个self参数已经通过super传入，故不用再传

s1 = Student('rendengbin','male','90')

#使用isinstance来判断一个变量的类型
print isinstance(s1,object)
print isinstance(s1,Person)
print isinstance(s1,Student)

#---------------------------
s2 = Person('xiaoguodong','male')
print isinstance(s2,object)
print isinstance(s2,Person)
print isinstance(s2,Student)

#总结
#1.派生类对象也是一个基类对象，反之不成立
#2.遵循is-a关系
