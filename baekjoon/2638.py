import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

hour = 0
air = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    global air

    visited[x][y] = True
    air += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if plate[nx][ny] == 0 and not visited[nx][ny]:
            dfs(nx, ny)


while air < N * M:
    air = 0
    visited = [[False] * M for _ in range(N)]
    dfs(0, 0)
    if air == N * M:
        print(hour)
        break
    melting = []
    for a in range(N):
        for b in range(M):
            if plate[a][b] == 1:
                cnt = 0
                for j in range(4):
                    na, nb = a + dx[j], b + dy[j]
                    if 0 <= na < N and 0 <= nb < M and visited[na][nb]:
                        cnt += 1
                if cnt >= 2:
                    melting.append([a, b])

    for a, b in melting:
        plate[a][b] = 0
    hour += 1
