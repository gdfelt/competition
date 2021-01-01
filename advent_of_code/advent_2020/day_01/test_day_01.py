
from advent_2020.day_01 import day_01

class TestAoC:
    def test_day1_part1(self):
        assert day_01.main(2) == 1020099

    def test_day1_part2(self):
        assert day_01.main(3) == 49214880

    