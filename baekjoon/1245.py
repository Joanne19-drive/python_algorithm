import sys

input = sys.stdin.readline

n, m = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

visited = [[False] * m for _ in range(n)]
cnt = 0


def dfs(x, y):
    global is_peak

    visited[x][y] = True

    for i in range(8):
        new_x, new_y = x + dx[i], y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < m:
            if farm[x][y] < farm[new_x][new_y]:
                is_peak = False
            if not visited[new_x][new_y] and farm[x][y] == farm[new_x][new_y]:
                dfs(new_x, new_y)


for a in range(n):
    for b in range(m):
        if farm[a][b] > 0 and not visited[a][b]:
            is_peak = True
            dfs(a, b)
            if is_peak:
                cnt += 1

print(cnt)
