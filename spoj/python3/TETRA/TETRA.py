#!/bin/python3
import math

## NOT SUBMITTED YET!!
# Still working on the irregular cases

def calc_insphere_rad( dimentions ):
	edges = dimentions.split()
	for e in edges:
		if int(e) == 0:
			return str("{:0.4f}".format(0))

	if edges[0] == edges[1] and edges[1] == edges[2] and edges[2] == edges[3] and edges[3] == edges[4] and edges[4] == edges[5]:
		rad = float(edges[0]) / math.sqrt(24)
		return str("{:0.4f}".format(rad))

def main():
	reps = int(input())
	for i in range(reps):
		print(calc_insphere_rad(input()))

if __name__ == "__main__":
	main()	