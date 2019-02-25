#!/bin/python3
def fact( num ):

	if(num <= 0):
		return 0

	if(num == 1):
		return 1

	if(num == 2):
		return 2

	total = 1
	for i in range(num, 1, -1):
		total *= i

	return total

reps = int(input())

for i in range(reps):
	print(fact(int(input())))