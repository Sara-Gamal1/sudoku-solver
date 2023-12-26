import numpy as np
# from timeout_decorator import timeout
# @timeout(120) 
def check(grid,N):
    rows = len(grid)
    cols = len(grid[0])

    # Check for same non-zero numbers in rows
    for row in grid:
        row_set = set()
        for num in row:
            if num != 0:
                if num in row_set:
                    return False  # Found the same non-zero number in the row
                row_set.add(num)

    # Check for same non-zero numbers in columns
    for j in range(cols):
        col_set = set()
        for i in range(rows):
            if grid[i][j] != 0:
                if grid[i][j] in col_set:
                    return False  # Found the same non-zero number in the column
                col_set.add(grid[i][j])
    return solveSudoku(grid,0,0,N) 
    # return True
 
    

def isSafe(grid, row, col, num,N):
    for x in range(N):
        if grid[row][x] == num:
            return False

    for x in range(N):
        if grid[x][col] == num:
            return False

    startRow = row - row % int(N**0.5)
    startCol = col - col % int(N**0.5)
    for i in range(int(N**0.5)):
        for j in range(int(N**0.5)):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def solveSudoku(grid, row, col,N):
    if row == N - 1 and col == N:
        return True

    if col == N:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1,N)

    for num in range(1, N + 1, 1):
        if isSafe(grid, row, col, num,N):
            grid[row][col] = num

            if solveSudoku(grid, row, col + 1,N):
                return True

        grid[row][col] = 0
    return False
