#!/bin/python3

import unittest
from . import TETRA


class TETRATestCase(unittest.TestCase):
    
    def test_tetra_regular_small(self):
    	self.assertEqual(TETRA.calc_insphere_rad("1 1 1 1 1 1"), "0.2041")
    
    def test_tetra_regular_big(self):
    	self.assertEqual(TETRA.calc_insphere_rad("1000 1000 1000 1000 1000 1000"), "204.1241")


if __name__ == '__main__':
    unittest.main()