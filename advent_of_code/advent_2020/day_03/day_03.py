class Day03(object):
    def __init__(self):
        self.data = []

        with open("advent_2020/day_03/day_03.dat") as file:
            for line in file:
                self.data.append(line.strip())

    def calc_slope(self, right, down):
        count = 0
        point = 0
        for x in range(0, len(self.data), down):
            if self.data[x][point] == "#":
                count += 1
            point += right
            point %= len(self.data[x])
        return count

    def part_01(self):
        return self.calc_slope(3, 1)

    """

    """

    def part_02(self):
        return (
            self.calc_slope(1, 1)
            * self.calc_slope(3, 1)
            * self.calc_slope(5, 1)
            * self.calc_slope(7, 1)
            * self.calc_slope(1, 2)
        )
