# -*- coding: utf-8 -*-

#1.tuple的元素不能改变
t=('Adam','Lisa','Bart')
print t

#2.tuple本身的元素不能被修改，但本身元素的值可以被修改
t1=('a','b',['A','B'])

#t1[2]即为tuple内的list
L=t1[2]

#可以修改list的值
L[0] = 'X'
L[1] = 'Y'
