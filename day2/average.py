#!/usr/bin/env python
# coding=utf-8

N = 10
sum = 0
count = 0
print("Please input 10 number:")
while count < N:
    number = float(input())
    sum = sum + number
    count = count + 1

average = sum / N;
print("Average = {:.2f}".format(average))
