#!/bin/python3

import unittest
from . import ONP

class ONPTestCase(unittest.TestCase):
    
    def test_rev_polish_notation_simple(self):
    	self.assertEqual(ONP.rev_polish_notation("(a+(b*c))"), "abc*+")
    
    def test_rev_polish_notation_long(self):
    	self.assertEqual(ONP.rev_polish_notation("((a+t)*((b+(a+c))^(c+d)))"), "at+bac++cd+^*")


if __name__ == '__main__':
    unittest.main()