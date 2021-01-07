
from day_01 import main

class TestAoC:
    def test_day1_part1(self):
        assert main(2) == 1020099

    def test_day1_part2(self):
        assert main(3) == 49214880

    