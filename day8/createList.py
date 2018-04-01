# -*- coding: utf-8 -*-

#简单的生成一个list

#1-10
range(1,11)

#1*1 - 10*10
L = []
for x in range(1,11):
    L.append(x*x)

#采用列表生成式
#1*2 3*4 - 99*100
print [x*(x+1) for x in range(1,100,2)]
