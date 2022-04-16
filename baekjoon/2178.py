import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
maze = [input() for _ in range(n)]
board = [[0] * m for _ in range(n)]

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]


def isValid(vis, x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if vis[x][y] != 0:
        return False
    if maze[x][y] == '0':
        return False
    return True


x, y = 0, 0
q = deque()

q.append([x, y])
board[x][y] = 1

while q:
    cell = q.popleft()
    a = cell[0]
    b = cell[1]
    for i in range(4):
        adja = a + dx[i]
        adjb = b + dy[i]
        if isValid(board, adja, adjb):
            q.append([adja, adjb])
            board[adja][adjb] = board[a][b] + 1

# 먼저 (N,M)에 도착한 최단경로의 값이 board[n-1][m-1]을 차지하기 때문에 뒤늦게 도착한 애들은 0이 아닌 board[n-1][m-1]값을 수정할 수 없음.
print(board[n-1][m-1])
