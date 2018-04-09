# -*- coding: utf-8 -*-

#如果想在python2中使用python3的功能
#则需要引入__future__中的模块

#1.python3中整数除法结果精确到小数
from __future__ import division
print 10/3

#2.python3中字符串统一为unicode,不需要加前缀u
#  而以字节存储的str则必须加前缀b

from __future__ import unicode_literals

s = 'am I an unicode?'
print isinstance(s,unicode)
