import sys

input = sys.stdin.readline
n, m = map(int, input().split())

light = [[] for _ in range(n+1)]
heavy = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    light[a].append(b)
    heavy[b].append(a)


def dfs(group, i):
    global cnt
    for child in group[i]:
        if not visited[child]:
            visited[child] = True
            cnt += 1
            dfs(group, child)


not_middle = 0

for i in range(1, n+1):
    visited = [False] * (n+1)
    cnt = 0
    dfs(light, i)
    if cnt >= (n+1) // 2:
        not_middle += 1
    cnt = 0
    dfs(heavy, i)
    if cnt >= (n+1) // 2:
        not_middle += 1

print(not_middle)
