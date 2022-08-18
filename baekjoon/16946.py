import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
whole_map = [list(input().rstrip()) for _ in range(N)]

ans = [''] * N
visited = [[False] * M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(start):
    q = deque()
    q.append(start)

    cnt = 1

    while q:
        a, b = q.popleft()
        whole_map[a][b] = group_num

        for c in range(4):
            na, nb = a + dx[c], b + dy[c]
            if 0 <= na < N and 0 <= nb < M:
                if whole_map[na][nb] == '0' and not visited[na][nb]:
                    visited[na][nb] = True
                    cnt += 1
                    q.append((na, nb))

    return cnt


def count_zero(a, b):
    cnt = 1
    v = set()  # 또 다른 visited를 쓰는 것보다 set를 쓰는 게 더 빠르다...
    for k in range(4):
        ni, nj = a + dx[k], b + dy[k]
        if 0 <= ni < N and 0 <= nj < M and whole_map[ni][nj] != '1':
            v.add(whole_map[ni][nj])
    for g_num in v:
        cnt += group[g_num]
    return cnt % 10


group = {}
group_num = 2

for i in range(N):
    for j in range(M):
        if whole_map[i][j] == '0' and not visited[i][j]:
            visited[i][j] = True
            group[group_num] = bfs((i, j))
            group_num += 1

for i in range(N):
    for j in range(M):
        if whole_map[i][j] == '1':
            ans[i] += str(count_zero(i, j))
        else:
            ans[i] += '0'

for a in ans:
    print(a)
