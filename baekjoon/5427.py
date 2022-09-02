import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs():
    while q:
        a, b = q.popleft()
        if visited[a][b] != 'F':
            flag = visited[a][b]
        else:
            flag = 'F'

        for i in range(4):
            na, nb = a + dx[i], b + dy[i]
            if 0 <= na < M and 0 <= nb < N:
                # visited[na][nb]가 0 이상이면 이미 상근이가 지나간 곳이기 때문에 불이 그 루트(route)로 따라온다고 한들 상근이를 잡을 수는 없음.
                # 따라서 해당 루트로 F가 오는 것은 고려하지 않음.
                if visited[na][nb] == -1 and building[na][nb] in ['.', '@']:
                    if flag == 'F':
                        visited[na][nb] = flag
                    else:
                        visited[na][nb] = flag + 1
                    q.append((na, nb))
            else:
                if flag != 'F':
                    return flag + 1

    return "IMPOSSIBLE"


for _ in range(T):
    N, M = map(int, input().split())
    building = [list(input().rstrip()) for i in range(M)]

    q = deque()
    visited = [[-1] * N for i in range(M)]
    start = (-1, -1)

    for x in range(M):
        for y in range(N):
            if building[x][y] == '@':
                visited[x][y] = 0
                start = (x, y)
            elif building[x][y] == '*':
                visited[x][y] = 'F'
                q.append((x, y))

    q.append(start)
    print(bfs())
