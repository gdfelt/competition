import re


class Day04(object):
    def __init__(self):
        self.pp_list = []
        with open("advent_2020/day_04/day_04.dat", "r") as file:
            data = file.read().split("\n\n")
            data = [d.replace("\n", " ") for d in data]
            for d in data:
                passport = {}
                for entry in d.split(" "):
                    passport[entry.split(":")[0]] = entry.split(":")[1]
                self.pp_list.append(passport)

    def fields_present(self, passport):
        return (
            "byr" in passport
            and "iyr" in passport
            and "eyr" in passport
            and "hgt" in passport
            and "hcl" in passport
            and "ecl" in passport
            and "pid" in passport
        )

    def fields_valid(self, passport):
        return (
            self.val_birthyear(passport["byr"])
            and self.val_issueyear(passport["iyr"])
            and self.val_expireyear(passport["eyr"])
            and self.val_eyecolor(passport["ecl"])
            and self.val_haircolor(passport["hcl"])
            and self.val_height(passport["hgt"])
        )

    def val_birthyear(self, value):
        return (
            value.isdigit()
            and len(value) == 4
            and int(value) >= 1920
            and int(value) <= 2002
        )

    def val_issueyear(self, value):
        return (
            value.isdigit()
            and len(value) == 4
            and int(value) >= 2010
            and int(value) <= 2020
        )

    def val_expireyear(self, value):
        return (
            value.isdigit()
            and len(value) == 4
            and int(value) >= 2020
            and int(value) <= 2030
        )

    def val_height(self, value):
        hgt_unit = value[-2:]
        hgt_value = value[:-2]
        # print(hgt_value, hgt_unit)
        if not (hgt_unit == "cm" or hgt_unit == "in"):
            return False
        if hgt_unit == "cm":
            return int(hgt_value) <= 193 and int(hgt_value) >= 150
        return int(hgt_value) <= 76 and int(hgt_value) >= 59

    def val_haircolor(self, value):
        p = re.compile("^#[0-9a-fA-F]{6}")
        if p.match(value):
            return True
        else:
            return False

    def val_eyecolor(self, value):
        return (
            value == "amb"
            or value == "blu"
            or value == "brn"
            or value == "gry"
            or value == "grn"
            or value == "hzl"
            or value == "oth"
        )

    # Passport ID

    # Country ID

    def part_01(self):
        count = 0
        for d in self.pp_list:
            count = count + 1 if self.fields_present(d) else count
        return count

    def part_02(self):
        count = 0
        for d in self.pp_list:
            if self.fields_present(d) and self.fields_valid(d):
                count += 1
        return count