# -*- coding: utf-8 -*-

#取list中的一部分

#笨方法
L = ['Adam','Lisa','Bart','Paul']

print [L[0],L[1],L[2]]

#采用循环
r = []
n = 3
for i in range(n):
    r.append(L[i])

print r

#取一个范围
print L[1:3]

#只用一个:，表示从头到尾
print L[:]

#第三个参数，每N个取一次
print L[::2]


#练习题
S = range(1,101)

print S[:10]
print S[2::3]
print S[4:50:5]

#逆序切片
L = range(1,101)
print L[-10:]
print L[4::5][-10:]
