import sys

input = sys.stdin.readline
T = int(input())


def distance(a, b):
    return (area[a][0] - area[b][0]) ** 2 + (area[a][1] - area[b][1]) ** 2


def dfs(i):
    visited[i] = True
    for j in range(N):
        if distance(i, j) <= (area[i][2] + area[j][2]) ** 2 and not visited[j]:
            dfs(j)


for _ in range(T):
    N = int(input())
    area = [list(map(int, input().split())) for i in range(N)]

    visited = [False] * N
    cnt = 0
    for i in range(N):
        if not visited[i]:
            cnt += 1
            dfs(i)
    print(cnt)
