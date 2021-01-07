import pytest
from day_02 import Day02

class TestAoC:

    @pytest.fixture
    def setup(self):
        return Day02()

    def test_parse_pwd(self, setup):
        assert setup.parse_pwd("3-7 q: qjxlgqd") == [3, 7, "q", "qjxlgqd"]
        assert setup.parse_pwd("4-6 w: fpbwwwwcwprflnjtwl") == [4, 6, "w", "fpbwwwwcwprflnjtwl"]

    def test_day2_part1(self, setup):
        assert setup.part_01() == 643

    def test_day2_part2(self, setup):
        assert setup.part_02() == 388

    