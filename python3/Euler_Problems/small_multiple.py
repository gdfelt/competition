#!/bin/python3



# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20



up_limit = 20
factors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

not_found = True

def check_value(num):
	for i in factors:
		if num % i != 0:
			return False
	return True


def small_multiple(up_limit):
	inc = 19 * 20
	value = inc
	while(not_found):
		if check_value(value):
			return value
		else:
			value += inc



def main():
	print(small_multiple(up_limit))

if __name__ == "__main__":
	main()