#! /usr/bin/env
#conding=utf-8

n = int(input("Enter the value of n:"))
print("Enter values for the Matrix A")
a = []#a是一个列表，保存二维矩阵
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print("After matrix multiplication")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5),end='')
    print()
print("-" * 7 * n)
