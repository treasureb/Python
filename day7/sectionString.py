# -*- coding: utf-8 -*-

#字符串切片

def firstCharUpper(s):
    return s[:1].upper()+s[1:]

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')
