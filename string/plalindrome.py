#! /usr/bin/env
#codind=utf-8

s = input("Please enter a string.")
z = s[::-1]
if s == z:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
