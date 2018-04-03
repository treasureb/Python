# -*- coding: utf-8 -*-

#sorted函数
L = [36,5,12,9,21]
print sorted(L)

#自定义排序
#如果x排在前面,返回-1
#如果x排在后面,返回1
#如果相等,返回0
def reversed_cmp(x,y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted(L,reversed_cmp)

#忽略大小写，对字符串排序
def cmp_ignore_case(s1,s2):
    return cmp(s1.lower(),s2.lower())

print sorted(['bob','about','Zoo','Creaate'],cmp_ignore_case)
