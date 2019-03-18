#!/usr/bin/env python3


def get_score(name):
	score = 0
	for c in name:
		score += ord(c) - 64
	return score


def main():
	list = {}
	with open('p022_names.dat') as file:
		list = file.read().replace("\"", "").split(",")
	list.sort()
	total = 0
	for index, l in enumerate(list, start=1):
		total += index * get_score(l)
		#print(str(index) + ": " + l + " " + str(get_score(l)))
	print(total)

if __name__ == "__main__":
	main()