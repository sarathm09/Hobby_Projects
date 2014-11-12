from turtle import *

def move(a, i):
	if a == 0:
		fd(i)
	elif a == 2:
		lt(i)
	elif a == 1:
		rt(i)
	move(a/3, i%100)

move(3, 23452352)