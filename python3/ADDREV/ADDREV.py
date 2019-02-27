#!/bin/python3

def reverse( user_in ):
	inp_arr = user_in.split()

	return str(int(inp_arr[0].strip('0')[::-1]) + int(inp_arr[1].strip('0')[::-1])).strip('0')[::-1]

def addrev():
	reps = int(input())
	for i in range(reps):
		print(reverse(input()))

if __name__ == "__main__":
	addrev()	