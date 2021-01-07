import pytest
from day_03 import Day03

class TestAoC:

    @pytest.fixture
    def setup(self):
        return Day03()

    def test_day3_part1(self, setup):
        assert setup.part_01() == 230

    def test_day3_part2(self, setup):
        assert setup.part_02() == 9533698720

   