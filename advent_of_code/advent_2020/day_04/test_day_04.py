import pytest
from day_04 import Day04


class TestAoC:
    @pytest.fixture
    def setup(self):
        return Day04()

    def test_invalid_pp(self, setup):
        assert (
            setup.fields_valid(
                {
                    "eyr": "1972",
                    "cid": "100",
                    "hcl": "#18171d",
                    "ecl": "amb",
                    "hgt": "170",
                    "pid": "186cm",
                    "iyr": "2018",
                    "byr": "1926",
                }
            )
            == False
        )

        assert (
            setup.fields_valid(
                {
                    "hcl": "dab227",
                    "iyr": "2012",
                    "ecl": "brn",
                    "hgt": "182cm",
                    "pid": "021572410",
                    "eyr": "2020",
                    "byr": "1992",
                    "cid": "277",
                }
            )
            == False
        )

    def test_valid_pp(self, setup):
        assert (
            setup.fields_valid(
                {
                    "pid": "087499704",
                    "hgt": "74in",
                    "ecl": "grn",
                    "iyr": "2012",
                    "eyr": "2030",
                    "byr": "1980",
                    "hcl": "#623a2f",
                }
            )
            == True
        )

        assert (
            setup.fields_valid(
                {
                    "eyr": "2029",
                    "ecl": "blu",
                    "cid": "129",
                    "byr": "1989",
                    "iyr": "2014",
                    "pid": "896056539",
                    "hcl": "#a97842",
                    "hgt": "165cm",
                }
            )
            == True
        )

    def test_day4_part1(self, setup):
        assert setup.part_01() == 204

    def test_day4_part2(self, setup):
        assert setup.part_02() == 179
