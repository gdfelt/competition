#!/usr/bin/env python
import scoring


def test_calc_score1():
    assert scoring.calc_score("2:1,1,2,2") == "2,6"

def test_calc_score2():
    assert scoring.calc_score("3:1,4,6,4,7,0") == "5,22,29"

def test_calc_score3():
    assert scoring.calc_score("3:0,0,9,1,0,0") == "0,10,10"


# Level 1 answers
def test_calc_score4():
    assert scoring.calc_score("3:1,2,6,4,5,2") == "3,18,25"

def test_calc_score5():
    assert scoring.calc_score("2:1,2,6,4,5") == "3,18"

def test_calc_score6():
    assert scoring.calc_score("1:2,8,5") == "15"

def test_calc_score7():
    assert scoring.calc_score("3:0,0,9,1,0,0") == "0,10,10"

# Level 2 answers
def test_calc_score8():
    assert scoring.calc_score("4:1,5,5,5,4,6,8,1") == "6,20,38,47"

def test_calc_score9():
    assert scoring.calc_score("3:1,5,5,5,4,6,8") == "6,20,38"


# Level 3 answers
def test_calc_score10():
    assert scoring.calc_score("3:1,4,10,2,5") == "5,22,29"

def test_calc_score11():
    assert scoring.calc_score("1:10,1,3") == "14"

def test_calc_score12():
    assert scoring.calc_score("3:3,4,10,1,2") == "7,20,23"

def test_calc_score13():
    assert scoring.calc_score("2:3,4,10,1,2") == "7,20"


# Level 4 answers
def test_calc_score14():
    assert scoring.calc_score("4:1,4,10,10,3,6") == "5,28,47,56"

def test_calc_score15():
    assert scoring.calc_score("3:10,10,10,3,6") == "30,53,72"

def test_calc_score16():
    assert scoring.calc_score("4:1,5,10,10,1,7") == "6,27,45,53"

def test_calc_score17():
    assert scoring.calc_score("3:1,5,10,10,1,7") == "6,27,45"

# Level 5 answers
def test_calc_score18():
    assert scoring.calc_score("3:1,4,10,7,3,8") == "5,25,43"

def test_calc_score19():
    assert scoring.calc_score("2:7,3,10,1,4") == "20,35"

def test_calc_score20():
    assert scoring.calc_score("4:2,7,10,4,6,4,5") == "9,29,43,52"

def test_calc_score21():
    assert scoring.calc_score("4:2,7,4,6,10,4,5") == "9,29,48,57"

def test_calc_score22():
    assert scoring.calc_score("3:2,7,4,6,10,4,5") == "9,29,48"


# Level 6 answers
def test_calc_score23():
    assert scoring.calc_score("10:1,4,4,5,6,4,5,5,10,0,1,7,3,6,4,10,2,8,6") == "5,14,29,49,60,61,77,97,117,133"

def test_calc_score24():
    assert scoring.calc_score("10:1,4,4,5,6,4,5,5,10,0,1,7,3,6,4,10,2,8,6") == "5,14,29,49,60,61,77,97,117,133"

def test_calc_score25():
    assert scoring.calc_score("10:0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0") == "0,0,0,0,0,0,0,0,0,0"

def test_calc_score26():
    assert scoring.calc_score("10:10,10,10,10,10,10,10,10,10,10,10,10") == "30,60,90,120,150,180,210,240,270,300"

def test_calc_score27():
    assert scoring.calc_score("10:7,2,1,9,6,4,5,5,10,3,7,7,3,6,4,10,2,8,6") == "9,25,40,60,80,97,113,133,153,169"

