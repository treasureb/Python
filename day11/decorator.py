# -*- coding: utf-8 -*-


#多个函数都要打印日志
#1.每个函数内使用print
#2.高阶函数,函数变量

#装饰器的作用
#1.打印日志:@log
#2.检测性能:@performance
#3.数据库事务:@transaction
#4.URL路由:@post('/register')·

#编写无参数decorator

#log定义
def log(f):
    def fn(x):
        print 'call ' + f._name_ + '()...'
        return f(x)
    return fn

#阶乘函数
@log
def factorial(n):
    return reduce(lambda x,y: x*y,range(1,n+1))
print factorial(10)


import time

def performance(f):
    def fn(*args,**kw):
        print 'call' + f._name_+'()...'+'time'+time.strtime('%Y-%m-%d',time.localtime(time.time()))
        return f(*args,**kw)
    return fn

@Performance
def factorial(n):
    return reduce(lambda x,y: x*y,range(1,n+1))
print factorial(10)
