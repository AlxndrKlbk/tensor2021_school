def find_next_cell_to_fill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def is_valid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here.
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solve_sudoku(grid, i=0, j=0):
    i, j = find_next_cell_to_fill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if is_valid(grid, i, j, e):
            grid[i][j] = e
            if solve_sudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False


sudoku_list = []
with open('input.txt', 'r') as file:
    for line in file:
        sudoku_list.append([int(val) for val in line.strip().split()])

print(sudoku_list)

solve_sudoku(sudoku_list)

output_list = []
for row in sudoku_list:
    output_list.append([str(val) for val in row])

with open('output.txt', 'w') as file:
    for item in output_list:
        line_string = " ".join(item)
        file.writelines(line_string + '\n')

