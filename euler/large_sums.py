#!/usr/bin/env python3



def process_line(s):
	return int(s[:12])

def main():
	sum_val = 0
	with open('large_sums.dat') as file:
		for line in file:
			sum_val += process_line(line)

	print(str(sum_val)[:10])

if __name__ == "__main__":
	main()