class Day05(object):
    def __init__(self):
        self.passes = []
        with open("advent_2020/day_05/day_05.dat", "r") as data:
            for l in data:
                self.passes.append(l.strip())

    def calc_seat(self, seat_string, seat_range):
        # print(seat_string, seat_range)
        lower, upper = seat_range

        for c in seat_string:
            if c == "F" or c == "L":
                upper -= (upper + 1 - lower) / 2
            elif c == "B" or c == "R":
                lower += (upper + 1 - lower) / 2
            else:
                print("unexpected input:", c)
                return -1
        # these values should be the same by now
        return int(lower)

    def part_01(self):
        highest = 0
        for line in self.passes:
            id = self.calc_seat(line[:7], (0, 127)) * 8 + self.calc_seat(
                line[7:], (0, 7)
            )
            if id > highest:
                highest = id
        return highest

    def part_02(self):
        pass_list = [int(x) for x in range(self.part_01())]
        for line in self.passes:
            id = self.calc_seat(line[:7], (0, 127)) * 8 + self.calc_seat(
                line[7:], (0, 7)
            )
            try:
                pass_list.remove(id)
            except ValueError:
                pass

        return pass_list.pop()