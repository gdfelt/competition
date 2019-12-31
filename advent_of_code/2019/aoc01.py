import math

def main_one():
    s = 0    # sum
    with open('./aoc01.dat') as file:
        for line in file:
            s += math.floor(int(line.split()[0]) // 3) - 2
    print(s)

def calc_fuel(n):
    if n <= 0:
        return 0
    else:
        return n + calc_fuel(n // 3 - 2)

def main_two():
    s = 0
    with open('./aoc01.dat') as file:
        for line in file:
            n = line.split()[0]
            s += calc_fuel(int(n) // 3 - 2)
    print(s)

if __name__ == "__main__":
    main_one()
    main_two()

