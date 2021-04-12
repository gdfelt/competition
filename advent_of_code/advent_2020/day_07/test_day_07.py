import pytest
from day_07 import Day07


class TestAoC:
    @pytest.fixture
    def setup(self):
        return Day07()

    def test_day7_part1(self, setup):
        assert setup.part_01() == 0

    def test_day7_part2(self, setup):
        assert setup.part_02() == 0
