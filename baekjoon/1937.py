import sys

sys.setrecursionlimit(10**9)
n = int(input())

bamboo = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dp(a, b):
    if visited[a][b]:
        return visited[a][b]

    all_high = True

    for i in range(4):
        x, y = a + dx[i], b + dy[i]
        if x < 0 or x >= n or y < 0 or y >= n:
            continue
        if bamboo[a][b] > bamboo[x][y]:
            all_high = False
            visited[a][b] = max(visited[a][b], dp(x, y) + 1)

    if all_high:
        visited[a][b] = 1

    return visited[a][b]


ans = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans = max(ans, dp(i, j))

print(ans)
