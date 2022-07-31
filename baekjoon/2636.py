import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 깊이 우선 탐색 카테고리에 있는 문제라서 dfs로 풀었는데 bfs로 풀 때 더 빠른 듯.


def answer():
    hour = 1
    cnt = 0

    def dfs(a, b):
        visited[a][b] = True

        for i in range(4):
            x, y = a + dx[i], b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if array[x][y] == 0 and not visited[x][y]:
                    dfs(x, y)

    def check(a, b):
        flag = False
        for i in range(4):
            x, y = a + dx[i], b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if visited[x][y]:
                    return True
        return False

    while cnt < n * m:
        visited = [[False] * m for _ in range(n)]
        new_cnt = 0
        dfs(0, 0)

        for a in range(n):
            for b in range(m):
                if array[a][b] != 0 and check(a, b):
                    array[a][b] = 0
                    new_cnt += 1

        if new_cnt == 0:
            return hour-1, cnt
        hour += 1
        cnt = new_cnt


hour, cnt = answer()
print(hour)
print(cnt)
