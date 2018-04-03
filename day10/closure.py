# -*- coding: utf-8 -*-

#python中的闭包
#内层函数引用外层函数的变量,然后返回内层函数的情况，称为闭包
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum

#闭包的特点:要正确使用闭包,确保引用的局部变量在函数返回后不能变
#希望一次返回3个函数,分别计算1*1,2*2,3*3
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count();
print f1(),f2(),f3()

#正确使用
def count():
    fs = []
    for i in range(1,4):
        def f(m = i):
            return m*m
        fs.append(f)
    return fs

f1,f2,f3 = count();
print f1(),f2(),f3()
