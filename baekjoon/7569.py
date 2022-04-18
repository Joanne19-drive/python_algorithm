import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
tomato = []

for box in range(h):
    b = [list(map(int, input().split())) for _ in range(n)]
    tomato.append(b)

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]


q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append([i, j, k])

while q:
    x, y, z = q.popleft()
    for i in range(6):
        adjx = x + dx[i]
        adjy = y + dy[i]
        adjz = z + dz[i]
        if 0 <= adjx < h and 0 <= adjy < n and 0 <= adjz < m and tomato[adjx][adjy][adjz] == 0:
            tomato[adjx][adjy][adjz] = tomato[x][y][z] + 1
            q.append([adjx, adjy, adjz])

impossible = False
day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                impossible = True
            day = max(day, tomato[i][j][k])

if impossible == True:
    print(-1)
else:
    print(day-1)
