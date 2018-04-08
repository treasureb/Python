#-*- coding: utf-8 -*-

#创建list
classmates=['Micheal','Bob','Tracy']

#访问list中的数据，依照下标访问
print classmates
print classmates[0]#打印Micheal
print classmates[-1]#打印倒数第一个元素Tracy

#往list中插入数据
#1. append()函数，追加在list尾部
classmates.append('Paul')

#2.insert()函数，第一个参数为索引，第二个参数为新元素
classmates.insert(1,'Maple')
print classmates

#从list中删除一个元素
#1.pop()函数默认删除最后一个元素
classmates.pop()
#2.pop(3),也可以接受一个参数，为待删除的下标
classmates.pop(3)
print classmates

#替换元素
classmates[0] = 'Maple'

#实例:交换第一名和倒数第一名
L=['Adam','Lisa','Bart']
L.insert(0,L.pop())
L.insert(1,L.pop())

#Lis也支持连接的操纵
L=[1,2,3,4,5]
print L+[6,7,8,9]
