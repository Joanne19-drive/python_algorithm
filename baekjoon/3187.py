import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

R, C = map(int, input().split())
farm = [list(input()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

wolf_alive, sheep_alive = 0, 0


def dfs(x, y):
    visited[x][y] = True

    wolf, sheep = 0, 0

    if farm[x][y] == 'v':
        wolf += 1
    elif farm[x][y] == 'k':
        sheep += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if farm[nx][ny] in ['.', 'v', 'k'] and not visited[nx][ny]:
                w, s = dfs(nx, ny)
                wolf += w
                sheep += s

    return wolf, sheep


for i in range(R):
    for j in range(C):
        if farm[i][j] in ['v', 'k'] and not visited[i][j]:
            wolf, sheep = dfs(i, j)
            if sheep > wolf:
                sheep_alive += sheep
            else:
                wolf_alive += wolf

print(sheep_alive, wolf_alive)
