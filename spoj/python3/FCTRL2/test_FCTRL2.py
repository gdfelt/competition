#!/bin/python3

import unittest
from . import FCTRL2

class FCTRLTestCase(unittest.TestCase):
    
    def test_factorial_small(self):
        self.assertEqual(FCTRL2.fact(5), 120)

    def test_factorial_big(self):
        self.assertEqual(FCTRL2.fact(100), 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)


if __name__ == '__main__':
    unittest.main()