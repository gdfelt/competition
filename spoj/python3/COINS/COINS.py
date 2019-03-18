#!/bin/python3

import math
import sys
import functools

@functools.lru_cache(maxsize=None)
def byteland_coin( coin_num ):
	if (math.floor(coin_num / 2) + math.floor(coin_num / 3) + math.floor(coin_num / 4)) > coin_num:
		return byteland_coin(math.floor(coin_num / 2)) + byteland_coin(math.floor(coin_num / 3)) + byteland_coin(math.floor(coin_num / 4))

	else:
		return coin_num

def main():
	for line in sys.stdin:
		print(byteland_coin(int(line)))

if __name__ == "__main__":
	main()