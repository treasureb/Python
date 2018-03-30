# -*- coding: utf-8 -*-

#递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print fact(100)

#汉诺塔问题

def move(n,a,b,c):
    if n == 1:
        print a,'-->',c
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
    return

move(4,'A','B','C')
