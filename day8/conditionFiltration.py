# -*- coding: utf-8 -*-

#条件过滤

L = [x * x for x in range(1,11) if x % 2 == 0]
print L

#isinstance(x,str)
#判断变量x是否是字符串

def toUppers(L):
    return [x.upper() for x in L if isinstance(x,str)]

print toUppers(['Hello','world',101])
