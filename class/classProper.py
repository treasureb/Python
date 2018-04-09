# -*- coding: utf-8 -*-

#创建类属性
#类似于C++中的静态成员变量

#类属性直接绑定在类上，所以访问类属性不需要创建实例
#所有实例拥有同一份类属性
class Person(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Person.count += 1

p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count
p3 = Person('Tim')
print Person.count

#类属性和实例属性名字冲突
#实例属性优先级高
#声明为__address私有时，外部不能访问
class Person(object):
    address = 'Earth'
    def __init__(self,name):
        self.name = name

p1 = Person('Bob')
p2 = Person('Alice')

print 'Person.address = ' + Person.address

p1.address = 'China'
print 'p1.address = ' + p1.address

print 'Person.address = ' + Person.address
print 'p2.address = ' + p2.address
