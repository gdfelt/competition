#!/usr/bin/env python3

limit = 1000

def main():
	sum = 0
	for i in range(1, limit+1):
		sum += i**i
	print(str(sum)[-10:])

if __name__ == "__main__":
	main()