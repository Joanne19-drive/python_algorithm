import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# dfs로 했더니 방향 벡터를 쓰면 메모리 초과가 나와서 bfs로 풂.


def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if paper[nx][ny] and not visited[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = True
                    queue.append([nx, ny])

    return cnt


pictures = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] and not visited[i][j]:
            pictures += 1
            max_size = max(max_size, bfs(i, j))

print(pictures)
print(max_size)
