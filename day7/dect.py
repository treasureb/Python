# -*- coding: utf-8 -*-

#迭代dect中的value
d = {'Adam':95,'Lisa':85,'Bart':59,'Paul':74}


#取value可以使用value()和itervalues()
#前者将dect转化为包含value的list
sum = 0.0
for num in d.itervalues():
    sum += num
print sum/len(d)

