import pytest
from day_07 import Day07



@pytest.fixture
def setup():
    return Day07()

def test_day2_part1(setup):
    assert setup.part_01() == 0

def test_day2_part2(setup):
    assert setup.part_02() == 0
