class Day04(object):
    def __init__(self):
        self.data = []
        with open("advent_2020/day_04/day_04.dat", "r") as file:
            self.data = file.read().split("\n\n")
            self.data = [d.replace("\n", " ") for d in self.data]

    def part_01(self):
        count = 0
        for d in self.data:
            passport = {}
            for entry in d.split(" "):
                passport[entry.split(":")[0]] = entry.split(":")[1]
            if (
                "byr" in passport
                and "iyr" in passport
                and "eyr" in passport
                and "hgt" in passport
                and "hcl" in passport
                and "ecl" in passport
                and "pid" in passport
            ):
                count += 1
        return count

    def part_02(self):
        return 0