#!/usr/bin/env python3

"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

digit = ["", "one", "two", "three", "four", "five",
			"six", "seven", "eight", "nine", "ten",
			"eleven", "twelve", "thirteen", "fourteen", "fifteen",
			"sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "fourty", 
			"fifty", "sixty", "seventy", "eighty", "ninty"]

up_limit = 1000

def get_english(num):
	string = ""
	if num > 0 and num <= 19:
		return digit[num]
	elif num // 100 == 0:
		return tens[num // 10] if num % 10 == 0 else tens[num // 10] + '-' + digit[num % 10]  
	elif num // 1000 == 0:
		return digit[num // 100] + ' hundred' if num % 100 == 0 else digit[num // 100] + ' hundred and ' + get_english(num % 100)
	elif num // 10000 == 0:
		return digit[ num // 1000] + ' thousand' if num % 1000 == 0 else digit[num // 1000] + ' thousand ' + get_english(num % 1000)

def main():
	count = 0 
	for i in range(1, up_limit + 1):
		count += len(get_english(i).replace('-', '').replace(' ', ''))
	print(count)

if __name__ == "__main__":
	main()