

class Day01(object):

    def __init__(self):
        self.data = []    
        path = "advent_2021/day_01.dat"
        with open(path) as file:
            for line in file: 
                self.data.append(int(line.strip()))

    def part_01(self):
        count = 0
        for ind, _ in enumerate(self.data):
            if self.data[ind] > self.data[ind - 1]:
                count += 1
        return count

    def part_02(self):
        count = 0

        return count