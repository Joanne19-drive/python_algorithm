import sys
from collections import deque as queue

input = sys.stdin.readline
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

q = queue()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])


def isValid(a, b):
    if a < 0 or a >= n or b < 0 or b >= m:
        return False
    if tomato[a][b] != 0:
        return False
    return True


while q:
    rotten = q.popleft()
    a = rotten[0]
    b = rotten[1]
    for i in range(4):
        adjx = a + dx[i]
        adjy = b + dy[i]
        if isValid(adjx, adjy):
            tomato[adjx][adjy] = tomato[a][b] + 1
            q.append([adjx, adjy])

min_date = []

for line in tomato:
    if 0 in line:
        min_date = [-1]
        break
    min_date.append(max(line) - 1)

print(max(min_date))
