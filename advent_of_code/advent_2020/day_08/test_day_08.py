import pytest
from day_08 import Day08


class TestDay08:
    @pytest.fixture
    def setup(self):
        return Day08()

    def test_part_01(self, setup):
        assert setup.part_01() == 1137

    def test_part_02(self, setup):
        assert setup.part_02() == 0