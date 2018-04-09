# -*- coding: utf-8 -*-

#class中定义的实例方法其实也是属性，实际上是一个函数对象
class Person(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def get_grade(self):
        return 'A'

p1 = Person('Bob',90)
print p1.get_grade()
#p1.get_grade返回的是一个函数对象
#p1.get_grade()才是方法调用

#方法也是属性，可以动态的添加到实例上
#调用types.MethodType()
import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.socre >= 60:
        return 'C'

class Person(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

p1 = Person('Bob',90)
p1.get_grade = types.MethodType(fn_get_grade,p1,Person)
print p1.get_grade()

p2 = Person('Alice',65)
#print p2.get_grade()


#思考下面的代码
class Person(object):
    def __init__(self,name,score):
        self.name = name
        self.socre = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob',90)
print p1.get_grade
print p1.get_grade()
#p1.get_grade为什么是函数而不是方法
#lambda:'A'等价于return'A',相当于一个函数f，那么f()='A'
#p1.get_grade=f
#p1.get_grade()=f()
