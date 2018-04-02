#-*- coding: utf-8 -*-

#map()接收一个函数f和一个list
#通过f一次作用在list的每个元素上

def f(x):
    return x*x
print map(f,[1,2,3,4,5,6,7,8,9])

def format_name(s):
    return s[0].upper()+s[1:].lower()

print map(format_name,['adma','LISA','barT'])
