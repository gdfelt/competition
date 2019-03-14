#!/usr/bin/env python3


grid = []
win_size = 4

def max_prod(x_cor, y_cor):
	local_max = -1
	# calc horizontal product
	if x_cor < (len(grid[0]) - win_size):
		hp = grid[x_cor][y_cor] * grid[x_cor + 1][y_cor] * grid[x_cor + 2][y_cor] * grid[x_cor + 3][y_cor] 
		if hp > local_max: local_max = hp
	# calc vertical product
	if y_cor < (len(grid) - win_size):
		vp = grid[x_cor][y_cor] * grid[x_cor][y_cor + 1] * grid[x_cor][y_cor + 2] * grid[x_cor][y_cor + 3]
		if vp > local_max: local_max = vp
	# calc SE diagnal product
	if (x_cor < (len(grid[0]) - win_size)) and (y_cor < (len(grid) - win_size)):
		sep = grid[x_cor][y_cor] * grid[x_cor + 1][y_cor + 1] * grid[x_cor + 2][y_cor + 2] * grid[x_cor + 3][y_cor + 3]
		if sep > local_max: local_max = sep
	# calc SW diagnal product
	if (x_cor > win_size - 1) and (y_cor < (len(grid) - win_size)):
		swp = grid[x_cor][y_cor] * grid[x_cor - 1][y_cor + 1] * grid[x_cor - 2][y_cor + 2] * grid[x_cor - 3][y_cor + 3]
		if swp > local_max: local_max = swp

	return local_max

def main():
	with open('product_grid.dat') as file:
		for index, l in enumerate(file):
			grid.append([int(n) for n in l.split()])

	cur_max = -1
	# run through indexes in grid
	for x in range(len(grid[0])):
		for y in range(len(grid)):
			max = max_prod(x, y)
			if max > cur_max:
				cur_max = max
	print(cur_max)

if __name__ == "__main__":
	main()