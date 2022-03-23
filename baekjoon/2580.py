sudoku = [list(map(int, input().split())) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def filtering(a, b):
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for m in range(9):
        if sudoku[a][m] in possible:
            possible.remove(sudoku[a][m])
        if sudoku[m][b] in possible:
            possible.remove(sudoku[m][b])

    three_col = 3 * (a//3)
    three_row = 3 * (b//3)
    for x in range(three_col, three_col+3):
        for y in range(three_row, three_row+3):
            if sudoku[x][y] in possible:
                possible.remove(sudoku[x][y])
    return possible


def dfs(n):
    if n == len(zero):
        for v in sudoku:
            print(*v)
        exit()
    i, j = zero[n]
    possible = filtering(i, j)
    for num in possible:
        sudoku[i][j] = num
        dfs(n+1)
        sudoku[i][j] = 0


dfs(0)
