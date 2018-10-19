#! /usr/bin/env
#coding=utf-8

mystr = str(input("Enter string:"))
s = []
for x in mystr:
    if x.isdigit():
        s.append(x)

print("".join(s))
