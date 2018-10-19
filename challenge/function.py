#! /usr/bin/env
#coding=utf-8

import sys

def Hours(m):
    hours = int(m / 60)
    minutes = int(m % 60)
    print("{} H,{} M".format(hours,minutes))

try:
    m = int(sys.argv[1])
    if m < 0:
        raise ValueError("A ValueError Happend.")
    else:
        Hours(m)
except ValueError:
    print("ValueError: Input number cannot be negative.")
