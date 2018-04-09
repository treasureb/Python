# -*- coding: utf-8 -*-

#python中的_init_()函数相当于c++中的构造函数
#会在创建实例的时候自动调用
#_init_(self)第一个参数相当于this指针，只不过要显示传

class Person(object):
    def __init__(self,name,gender,birth,**kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k,v in kw.items():
            setattr(self,k,v)

xiaoming = Person('XiaoMing','Male','1996-09-16',job='Student')

print xiaoming.name
print xiaoming.job


#1.setaddr函数
#2.items遍历
