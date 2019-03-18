#!/bin/python3
import math

def test_num( num ):
	s = str(num)
	for i in range(0, math.floor(len(s) / 2)):
		if(s[i] != s[len(s) - 1 - i]):
			return False
	return True

def next_palin( start_num ):
	not_found = True
	num = int(start_num) + 1
	
	while not_found:
		s = str(num)
		if test_num(s):
			not_found = False
		else:
			num += 1
	return num

def main():
	reps = int(input())
	for i in range(reps):
		print(next_palin(input()))

if __name__ == "__main__":
	main()	