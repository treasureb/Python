# -*- coding: utf-8 -*-

#索引迭代->enumerate()函数
L = ['Adam','Lisa','Bart','Paul']
for index,name in enumerate(L):
    print index,'-',name


#zip()函数，合并两个list
L = ['Adam','Lisa','Bart','Paul']
K = zip([1,2,3,4],L)
for index,name in K:
    print index,'-',name
