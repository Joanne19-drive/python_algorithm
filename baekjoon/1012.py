import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline
t = int(input())


def dfs(a, b):
    if visited[b][a] == False:
        visited[b][a] = True
        if farm[b][a] == 1:
            if b > 0:
                dfs(a, b-1)
            if a > 0:
                dfs(a-1, b)
            if b < n-1:
                dfs(a, b+1)
            if a < m-1:
                dfs(a+1, b)


for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0] * m for i in range(n)]
    visited = [[False] * m for i in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
    count = 0
    for a in range(m):
        for b in range(n):
            if visited[b][a] == False:
                if farm[b][a] == 1:
                    count += 1
                    dfs(a, b)
    print(count)
