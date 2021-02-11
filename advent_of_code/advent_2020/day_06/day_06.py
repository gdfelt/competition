class Day06(object):
    def __init__(self):
        self.data = []
        with open("advent_2020/day_06/day_06.dat") as file:
            self.data = file.read().split("\n\n")
            self.data = [d.replace("\n", "") for d in self.data]

    def part_01(self):
        count = 0
        for d in self.data:
            count += len(set(d))
        return count

    def part_02(self):
        return 0