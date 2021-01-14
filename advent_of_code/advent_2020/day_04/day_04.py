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
        # Birthyear validation
        if not (
            passport["byr"].isdigit()
            and len(passport["byr"]) == 4
            and int(passport["byr"]) >= 1920
            and int(passport["byr"]) <= 2002
        ):
            return False

        # Issue Year
        if not (
            passport["iyr"].isdigit()
            and len(passport["iyr"]) == 4
            and int(passport["iyr"]) >= 2010
            and int(passport["iyr"]) <= 2020
        ): 
            return False

        # Exp Year
        if not (
            passport["eyr"].isdigit()
            and len(passport["eyr"]) == 4
            and int(passport["eyr"]) >= 2020
            and int(passport["eyr"]) <= 2030
        ): 
            return False

        # Height

        # Hair Color
        # if not (

        # ):
        #     return False

        # Eye Color
        if not (
            passport["ecl"] == "amb"
            or passport["ecl"] == "blu"
            or passport["ecl"] == "brn"
            or passport["ecl"] == "gry" 
            or passport["ecl"] == "grn"
            or passport["ecl"] == "hzl" 
            or passport["ecl"] == "oth" 
        ):
            return False

        # Passport ID
        
        return True

    def part_01(self):
        count = 0
        for d in self.pp_list:
            if self.fields_present(d):
                count += 1
        return count

    def part_02(self):
        count = 0
        for d in self.pp_list:
            if self.fields_present(d) and self.fields_valid(d):
                count += 1
        return count