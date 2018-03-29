# -*- coding:utf-8 -*-

import math
def move(x,y,step,angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny

#看似返回两个值，其实是一个tuple
x,y = move(100,100,60,math.pi /6)
print x,y

r = move(100,100,60,math.pi /6)
print r

#求一元二次方程
import math

def quadratic_equation(a,b,c):
    x = b*b-4*a*c
    if x < 0:
        return none
    elif x == 0:
        return -b/2*a
    else:
        return ((-b+math.sqrt(b*b-4*a*c))/(2*a),((-b-math.sqrt(b*b-4*a*c))/(2*a)))

print quadratic_equation(2,3,0)
print quadratic_equation(1,-6,5)
