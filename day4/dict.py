# -*- coding: utf-8 -*-
d = {
    'Adam' : 95,
    'Lisa' : 85,
    'Bart' : 59,
    'Paul' : 75
}
print d

#笨办法
print 'Adam:' + str(d.get('Adam'))
print 'Lisa:' + str(d.get('Lisa'))
print 'Bart:' + str(d.get('Bart'))
print 'Paul:' + str(d.get('Paul'))

print '------------------------'
#通过迭代器
for (key,value) in d.items():
    print("%s:%s" %(key,value))

#两个打印的顺序不同

#dict的特点
#1.查找速度快，K-V模型
#2.没有顺序存储
#3.key值不可变


#更新dict
d['maple'] = 100
print d
