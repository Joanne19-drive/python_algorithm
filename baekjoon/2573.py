import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def answer():
    global array

    cnt = 0
    year = 1

    def dfs(a, b):
        visited[a][b] = True

        sea = 0
        for i in range(4):
            if before[a+dx[i]][b+dy[i]] == 0:
                sea += 1
            else:
                if not visited[a+dx[i]][b+dy[i]]:
                    dfs(a+dx[i], b+dy[i])

        after[a][b] = before[a][b] - sea
        if after[a][b] < 0:
            after[a][b] = 0

    while cnt < 2:
        cnt = 0
        visited = [[False] * m for _ in range(n)]
        before = array[:]
        after = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if before[i][j] != 0 and not visited[i][j]:
                    cnt += 1
                    dfs(i, j)
        if cnt == 0:
            return 0
        if cnt >= 2:
            return year-1
        array = after[:]
        year += 1


print(answer())
