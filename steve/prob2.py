
# Rotates a 2D grid counter-clockwise
def rotate(grid):
    rotated = []
    for x in range(len(grid[0]) -1, -1, -1):
        r = []
        for y in range(0, len(grid)):
            r.append(grid[y][x])
        rotated.append(r)
    return rotated

def main():

    grid = [[1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]

    out = ""
    while(True):
        for n in grid.pop(0):
            out += str(n) + " "

        if(len(grid) == 0):
            break
        else:
            grid = rotate(grid)

    print(out)

if __name__ == "__main__":
    main()

