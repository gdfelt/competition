import pytest
from day_06 import Day06


class TestAoC:
    @pytest.fixture
    def setup(self):
        return Day06()

    def test_day6_part1(self, setup):
        assert setup.part_01() == 6799

    def test_day6_part2(self, setup):
        assert setup.part_02() == 0
