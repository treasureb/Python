# -*- coding: utf-8 -*-

#set的for循环遍历

s = set([('Adam',95),('Lisa',85),('Bart',59)])
for (name,score) in s:
    print name,':',score

#更新set

#添加新元素
s = set([1,2,3])
s.add(4)
#添加的元素如果已经存在，不会报错，但不会插进去

#删除元素
s.remove(4)
#如果删除的元素不在set内，则报错


#练习
s = set(['Adam','Lisa','Paul'])
L = ['Adam','Lisa','Bart','Paul']
for name in L:
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print s


