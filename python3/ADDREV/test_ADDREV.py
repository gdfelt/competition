#!/bin/python3

import unittest
from . import ADDREV

class ADDREVTestCase(unittest.TestCase):
    
    def test_add_reverse_small(self):
    	self.assertEqual(ADDREV.reverse("4358 754"), "1998")

    def test_add_reverse_one(self):
    	self.assertEqual(ADDREV.reverse("305 794"), "1")

if __name__ == '__main__':
    unittest.main()