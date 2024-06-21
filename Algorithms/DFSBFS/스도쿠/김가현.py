import sys
input = sys.stdin.readline

def check_row(row, n):
    for i in range(9):
        if n == board[row][i]:
            return False
    return True
def check_col(col, n):
    for i in range(9):
        if n == board[i][col]:
            return False
    return True

def check_rect(row, col, n):
    real_row = row // 3 * 3
    real_col = col // 3 * 3
    for y in range(3):
        for x in range(3):
            if n == board[real_row + y][real_col + x]:
                return False
    return True

board = [[] for _ in range(9)]
empty = []  #[(row,col)]

for n in range(9):
    for m, num in enumerate([int(x) for x in input().split()]):
        board[n].append(num)
        if num == 0:
            empty.append((n, m))

def dfs(n):
    if n == len(empty):
        for i in range(9):
            print(board[i])
        return

    row = empty[n][0]
    col = empty[n][1]

    for i in range(1, 10):
        if check_row(row, i) and check_col(col, i) and check_rect(row, col, i):
            board[row][col] = i
            dfs(n + 1)
            board[row][col] = 0

dfs(0)
