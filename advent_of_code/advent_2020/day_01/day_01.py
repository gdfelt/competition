from itertools import combinations
import math

def main(nums):
    with open('advent_2020/day_01/day_01.dat') as data:
        lines = [int(line.rstrip()) for line in data]
        comb = combinations(lines, nums)
        for c in list(comb):
            if sum(c) == 2020:
                return math.prod(c)
        
if __name__ == "__main__":
    main(2)