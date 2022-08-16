import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)  # recursionlimit을 몇으로 설정하느냐에 따라 메모리 초과가 뜰 수 있다,,,

N, Q = map(int, input().split())
N = 2 ** N
board = [list(map(int, input().split())) for _ in range(N)]
levels = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def firestorm(board, level):
    next = [[0] * (N) for _ in range(N)]
    for a in range(0, N, level):
        for b in range(0, N, level):
            for i in range(level):
                for j in range(level):
                    next[a+j][b+level-1-i] = board[a+i][b+j]

    melt = []

    for x in range(N):
        for y in range(N):
            if next[x][y] == 0:
                continue
            melting_count = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and next[nx][ny] > 0:
                    melting_count += 1
            if melting_count < 3:
                melt.append((x, y))

    for x, y in melt:
        next[x][y] -= 1

    return next


for l in levels:
    level = 2**l

    board = firestorm(board, level)

print(sum(sum(i) for i in board))


def dfs(x, y):
    cnt = 1
    board[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0:
            cnt += dfs(nx, ny)

    return cnt


max_ice = 0

for x in range(N):
    for y in range(N):
        if board[x][y] > 0:
            max_ice = max(max_ice, dfs(x, y))

print(max_ice)
