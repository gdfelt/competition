

class Day03(object):

    def __init__(self):
        self.data = []

        with open('advent_2020/day_03/day_03.dat') as file:
            for line in file:
                self.data.append(line.strip())


    def part_01(self):
        count = 0
        point = 0
        for line in self.data:
            if line[point] == '#':
                count+=1
            point+=3
            point%=len(line)

        return count

    def part_02(self):
        return 0