import pytest
from day_04 import Day04


class TestAoC:
    @pytest.fixture
    def setup(self):
        return Day04()

    def test_day4_part1(self, setup):
        assert setup.part_01() == 204

    def test_day4_part2(self, setup):
        assert setup.part_02() == 1
