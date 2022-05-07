import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline
m, n = map(int, input().split())
travel = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1] * n for _ in range(m)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def check(x, y):
    if x == m-1 and y == n-1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if travel[x][y] > travel[nx][ny]:
                visited[x][y] += check(nx, ny)
    return visited[x][y]


print(check(0, 0))
