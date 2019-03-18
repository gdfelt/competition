#!/usr/bin/env python3




def main():
	s = '0b1' + '0' * 1000
	print(int(s, 2))
	total = 0
	for c in str(int(s, 2)):
		total += int(c)
	print(total)

if __name__ == "__main__":
	main()