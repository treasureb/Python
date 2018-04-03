# -*- coding: utf-8 -*-

#python中函数可以返回函数

#注意区分返回函数和返回值
def myabs():
    return abs #返回函数
def myabs2(x):
    return abs(x)#返回值

#返回函数可以延迟计算
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum
#打印f并不能打印出结果
#打印f()的对象
f = calc_sum([1,2,3,4])
print f()

#编写函数，接收一个list，返回一个函数，返回函数可以计算参数的乘积
def calc_prod(lst):
    def cala():
        def prod(x,y):
            return x*y
        return reduce(prod,lst)
    return cala
f = calc_prod([1,2,3,4])
print f()
