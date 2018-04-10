# -*- coding: utf-8 -*-

#1.isinstance()判断它是否是某一类型的实例
#2.type()函数获取变量的类型
#3.dir()函数获取变量的所有属性->返回的属性为字符串列表


#如果已知一个属性名称,要获取或者设置对象的属性,使用
#1.获取geyattr()
#2.设置setattr()

#示例
class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student,my name is %s' % self.name

#print type(123)
s = Student('Bob','Male',88)
#print type(s)
#print dir(123)
#print dir(s) #dir返回实例变量的所有属性

#getattr和setattr的使用
#getattr(s,'name','maple')
#1.第一个参数为对象名
#2.第二个参数为对象的属性
#3.第三个参数为属性不存在,给定一个default
print getattr(s,'name')
print getattr(s,'age',20)

#setattr->设置新的属性
setattr(s,'name','Adam')
print s.name


#希望除了name和gender外,可以提供任意额外的关键字参数并绑定到实例
class Person(object):
    def __init__(self,name,gender,**kw):
        self.name = name
        self.gender = gender
        for k,v in kw.items():
            setattr(self,k,v)  #等价于self.k=v

p = Person('Bob','Male',age=18,course='Payrhon')
print p.age
print p.course
