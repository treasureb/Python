# -*- coding: utf-8 -*-

N = 10
x = 0
while x < N:
    print x
    x = x + 1

#求100以内奇数的和
sum = 0
i = 1
while i <= 100:
    sum += i
    i = i + 2
print sum

#break的使用
sum = 0
x = 1
while True:
    sum = sum + x
    x += 1
    if x > 100:
        break
print sum

#continue的使用
L = [75,98,59,81,66,43,69,85]
sum = 0.0
n = 0
for x in L:
    sum += x
    n += 1
print sum/n

#只想统计及格的
L = [75,98,59,81,66,43,69,85]
sum = 0.0
n = 0
for x in L:
    if x < 60:
        continue
    sum += x
    n += 1
print sum/n

#0-100以内奇数的和
sum = 0
x = 0
while True:
    if x >= 100:
        break
    x += 1
    if x%2 == 0:
        continue
    sum += x
print sum

#多重循环
#100以内个位数大于十位数的数字
for x in range(1,9):
    for y in range(x+1,10):
        print str(x)+str(y)
