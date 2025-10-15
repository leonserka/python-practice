# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:51:23 2023

@author: Student
"""

a=int(input("Unesi broj: "))
b=int(input("Unesi broj: "))
while a>0 and b>0:
    if a>b:
        for x in range(b+1,a):
            print(x)
        a = int(input("Unesi broj: "))
        b = int(input("Unesi broj: "))
    elif b>a:
        for y in range(a+1,b):
            print(y)
        a = int(input("Unesi broj: "))
        b = int(input("Unesi broj: "))
    else:
        print("Nema brojeva između njih.")
        a = int(input("Unesi broj: "))
        b = int(input("Unesi broj: "))
print("Greška, oba dva broja moraju biti pozitivna.")