#!/usr/bin/env python3

"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

#		        J   F   M   A   M   J   J   A   S   O   N   D
months = 	  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def main():
	day_ind = 0
	running_count = 0
	for year in range(1900, 2001):
		if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
			# leap year
			for index, month in enumerate(months_leap):
				day_ind += month % 7
				day_ind %= 7
				if day_ind == 6 and year > 1900:
					running_count += 1
		else:
			# regular year
			for index, month in enumerate(months):
				day_ind += month % 7
				day_ind %= 7
				if day_ind == 6 and year > 1900:
					running_count += 1
	print(running_count)

if __name__ == "__main__":
	main()