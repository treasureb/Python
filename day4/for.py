# -*- coding: utf-8 -*-

L = ['Adam','Lisa','Bart']
print L[0]
print L[1]
print L[2]


print u'使用for循环'

#一次去除L中的值放入name变量
#name是在for循环内部定义的变量
for name in L:
    print name

#求平均数
L = [75,92,59,68]
sum = 0.0
for data in L:
    sum += data
sum /= 4
print sum
