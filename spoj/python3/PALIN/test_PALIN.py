#!/bin/python3

import unittest
from . import PALIN

class PALINTestCase(unittest.TestCase):

	def test_next_palin_simple(self):
		self.assertEqual(PALIN.next_palin(808), 818)

	def test_next_palin_another_simple(self):
		self.assertEqual(PALIN.next_palin(2133), 2222)

	def test_next_palin_big(self):
		self.assertEqual(PALIN.next_palin(123999500), 124000421)

	def test_next_palin_nines(self):
		self.assertEqual(PALIN.next_palin(99999999999999), 100000000000001)

if __name__ == '__main__':
    unittest.main()


