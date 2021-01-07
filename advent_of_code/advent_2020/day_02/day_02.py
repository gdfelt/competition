class Day02(object):
    def __init__(self):
        self.data = []
        self.count = 0

        with open("advent_2020/day_02/day_02.dat") as file:
            for line in file:
                self.data.append(self.parse_pwd(line.strip()))

    """
    Returns parsed fields into an array
    e.x.
    3-7 q: qjxlgqd  => [3, 7, "q", "qjxlgqd"]
    """

    def parse_pwd(self, policy_line):
        policy, pw = policy_line.split(":")
        pw = pw.strip()

        # Parse policy part
        minmax, target = policy.split(" ")
        min, max = minmax.split("-")

        return [int(min), int(max), str(target), str(pw)]

    def part_01(self):
        for d in self.data:
            if d[3].count(d[2]) >= d[0] and d[3].count(d[2]) <= d[1]:
                self.count += 1
        return self.count

    def part_02(self):
        for d in self.data:
            if (d[3][d[0] - 1] == d[2]) ^ (d[3][d[1] - 1] == d[2]):
                self.count += 1
        return self.count
