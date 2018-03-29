# -*- coding:utf-8 -*-

#set只关注key,不关注value
#set不允许重复的值，具有去重功能

s=set(['Adam','Lisa','Bart','Paul'])
print s

#查询set中的元素使用in操作符

#如何可以不区分大小写
print 'Bart' in s
print 'bart' in s

#全部改为小写
s=set([name.lower() for name in ['Adam','Lisa','Bart','Paul']])
print 'Bart' in s
print 'bart' in s

