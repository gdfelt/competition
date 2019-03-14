#!/usr/bin/env python3

num_prods = 13

def calc_prod(ss):
	prod = 1
	for c in ss:
		prod *= int(c)
	return prod

def main():
	with open('large_prods.dat') as file:
		line = file.read()
		max_prod = 0
		max_index = 0
		for i in range(len(line) - num_prods + 1):
			ss = line[i:i+num_prods]
			#print(str(i) + ': ')
			if "0" in ss:
				continue
			if calc_prod(ss) > max_prod:
				max_prod = calc_prod(ss)
				max_index = i
	#print(max_index)
	print(max_prod)

if __name__ == "__main__":
	main()