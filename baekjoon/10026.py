import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
rgb = [list(input().rstrip()) for _ in range(n)]

# bfs로 풀다가 시간초과. 결국 dfs로 풀었음.
visited = [[False] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(a, b):
    visited[a][b] = True

    for i in range(4):
        x, y = a + dx[i], b + dy[i]
        if 0 <= x < n and 0 <= y < n and not visited[x][y]:
            if rgb[x][y] == rgb[a][b]:
                dfs(x, y)


rgb_count, gb_count = 0, 0

for a in range(n):
    for b in range(n):
        if not visited[a][b]:
            rgb_count += 1
            dfs(a, b)


visited = [[False] * n for _ in range(n)]

# dfs 함수에서 적록색약인지 아닌지 판별하여 다음 dfs로 넘기는 것보다 차라리 그래프에 있는 R을 다 G로 바꾸는게 시간초과 안남.
for a in range(n):
    for b in range(n):
        if rgb[a][b] == 'R':
            rgb[a][b] = 'G'

for a in range(n):
    for b in range(n):
        if not visited[a][b]:
            gb_count += 1
            dfs(a, b)

print(rgb_count, gb_count)
