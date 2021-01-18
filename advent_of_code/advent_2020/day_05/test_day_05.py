import pytest
from day_05 import Day05


class TestAoC:
    @pytest.fixture
    def setup(self):
        return Day05()

    def test_calc_seat(self, setup):
        assert setup.calc_seat("F", (0, 1)) == 0
        assert setup.calc_seat("B", (0, 1)) == 1
        assert setup.calc_seat("FBF", (0, 7)) == 2
        assert setup.calc_seat("BFFFBBF", (0, 127)) == 70
        assert setup.calc_seat("RRR", (0, 7)) == 7

    def test_day5_part1(self, setup):
        assert setup.part_01() == 828

    def test_day5_part2(self, setup):
        assert setup.part_02() == 0
