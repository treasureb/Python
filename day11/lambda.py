# -*- coding: utf-8 -*-

#匿名函数
map(lambda x:x * x,[1,2,3,4,5,6,7,8,9])
print map

#匿名函数的限制
#1.只能有一个表达式
#2.不写return

sorted([1,3,9,5,0],lambda x,y:-cmp(x,y))
print sorted

#返回匿名函数
myabs = lambda x: -x if x < 0 else x

#使用匿名函数简化代码
def is_not_empty(s):
    return s and len(s.strip()) > 0

print filter(is_not_empty,['test',None,'','str',' ','END'])
#简化后
#print filter(lambda s: s and len(s.strip()) > 0,['test',None,'','str',' ','END']
