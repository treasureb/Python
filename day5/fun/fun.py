# -*- coding: utf-8 -*- 

#abs()求绝对值函数

#cmp()比较函数

#int()强转为int

#str()强转为str

L = []
for x in range(1,101):
    L.append(x*x);
print sum(L)

def square_of_sum(L):
    return sum(num*num for num in L)

print square_of_sum([1,2,3,4,5])
print square_of_sum([-5,0,5,15,25])
