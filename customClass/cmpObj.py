# -*- coding: utf-8 -*-

#对非内置数据类型排序,提供特殊方法__cmp__()
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s,%s)' % (self.name,self.score)
    __repr__ = __str__

    def __cmp__(self,s):
        if self.name < s.name:
            return -1
        elif self.name > s.name:
            return 1
        else:
            return 0

L = [Student('Time',99),Student('Bob',88),Student('Alice',77)]
print sorted(L)


#修改上面的函数,先比较分数，如果分数相同则比较名字
def __cmp__(self,s):
    if self.score == s.score:
        return cmp(self.name,s.name)
    return -cmp(self.score,s.score)
