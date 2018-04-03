# -*- coding: utf-8 -*-

#reduce函数
#和map类似，接受一个函数f,一个list
#reduce中的函数f必须接收两个参数

def f(x,y):
    return x+y

print reduce(f,[1,3,5,7,9])

#reduce可以接受第三个参数作为初始值
print reduce(f,[1,3,5,7,9],100)
