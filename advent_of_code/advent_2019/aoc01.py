import math
import os

def main_one():
    s = 0    # sum
    with open('advent_2019/aoc01.dat') as file:
        for line in file:
            s += math.floor(int(line.split()[0]) // 3) - 2
    return s

def calc_fuel(n):
    if n <= 0:
        return 0
    else:
        return n + calc_fuel(n // 3 - 2)

def main_two():
    s = 0
    with open('advent_2019/aoc01.dat') as file:
        for line in file:
            n = line.split()[0]
            s += calc_fuel(int(n) // 3 - 2)
    return s

if __name__ == "__main__":
    main_one()
    main_two()

