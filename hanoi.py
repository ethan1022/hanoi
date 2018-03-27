#!/usr/bin/python3
# -*- coding: utf-8 -*-

def hanoi(n,a,b,c):
	if n == 1:
		print (a, "-->", c)
	else:
		hanoi(n-1, a, c, b) #將n-1層，從a放到b
		hanoi(1, a, b, c) #將最後1層，從a放到c
		hanoi(n-1, b, a, c) #將n-1層，從b放到c

n = int(input("輸入河內塔的層數： "))
hanoi(n,"A","B","C")

