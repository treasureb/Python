# -*- coding: utf-8 -*-

#多层表达式

L = [m+n for m in 'ABC' for n in '123']
print L

#上面的代码等价于
L = []
for m in 'ABC':
    for n in '123':
        L.append(m+n)
print L

#找出三位数的回文数

#1. 三成for循环
print [x+y*10+z*100 for x in range(1,10) for y in range(0,10) for z in range(1,10) if x == z]

#2.0
print [x for x in range(100,1000) if x/100 == x % 10]
