#!/usr/bin/env python3

"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

def get_score(name):
	score = 0
	for c in name:
		score += ord(c) - 64
	return score


def main():
	list = {}
	with open('resources/names.txt') as file:
		list = file.read().replace("\"", "").split(",")
	list.sort()
	total = 0
	for index, l in enumerate(list, start=1):
		total += index * get_score(l)
		#print(str(index) + ": " + l + " " + str(get_score(l)))
	print(total)

if __name__ == "__main__":
	main()