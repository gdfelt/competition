#!/usr/bin/env python3

"""
Project Euler Problem 42
========================

The n-th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

def main():
	# build list of triangle numbers
	# length of 20 covers 99.9% of enlgish words
	tri_numbers = []
	for x in range(1, 21):
		tri_numbers.append(int(.5 * x * (x + 1)))
	word_count = 0
	with open('resources/words.txt') as file:
		word_list = file.read().replace("\"", "").split(",")
		for word in word_list:
			word_sum = 0
			for c in word:
				word_sum += ord(c) - 64
			if word_sum in tri_numbers:
				word_count += 1
	print(word_count)

if __name__ == "__main__":
	main()