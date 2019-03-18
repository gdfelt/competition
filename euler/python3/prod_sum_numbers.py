#!/bin/python3

import functools


#	k:	n:	
#
#	2	4	2,2 
#	3	6	1,2,3
#	4	8	1,1,2,4
# 	5	8	1,1,2,2,2
# 	6	12	1,1,1,1,2,6
#	7	12	1,1,1,1,1,3,4	
#	8	12	1,1,1,1,1,2,2,3
#	9	18?	1,1,1,1,1,1,1,2,9 
# 	10	16? 1,1,1,1,1,1,1,1,4,4
#	11
#	12
#	13	
#	14


@functools.lru_cache(maxsize=None)
def fact( num ):
	fact_list = sorted(set(functools.reduce(list.__add__,([i, num//i] for i in range(2, int(num**0.5) + 1) if num % i == 0))))
	return fact_list

#def calc_fact_sets( factor_list ):
	# 

def min_prod_sum( k ):
	for i in range(k, 2*k+1):
		if(i % 2 == 1):
			continue
		print(i)
		print(fact(i))



if __name__ == "__main__":
	min_prod_sum(12)	
	#print(fact.cache_info())




