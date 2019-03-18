#!/bin/python3

import unittest
from . import COINS

class COINSTestCase(unittest.TestCase):
    
    def test_coins_small(self):
    	self.assertEqual(COINS.byteland_coin(100), 120)

    def test_coins_big(self):
    	self.assertEqual(COINS.byteland_coin(987876765), 4241507870)

if __name__ == '__main__':
    unittest.main()