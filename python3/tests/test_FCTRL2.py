import unittest
from unittest.mock import patch
import FCTRL2

class FCTRLTestCase(unittest.TestCase):
    
    @mock.patch('builtins.print')
   	def test_factorial(self):
		input = [
			'4',
			'1',
			'2',
			'5',
			'3'
		]

		expected = [
			1,
			2,
			120,
			6
		]

		with patch('builtins.input', side_effect=input):
			FCTRL2.fctrl2()



if __name__ == '__main__':
    unittest.main()