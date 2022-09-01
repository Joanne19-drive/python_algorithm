import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
visited[0][0] = True

max_move = 0


def dfs(x, y, cnt):
    global max_move

    move = int(board[x][y])
    dx = [0, 0, move, -move]
    dy = [move, -move, 0, 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 'H' and cnt + 1 > dp[nx][ny]:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dp[nx][ny] = cnt + 1
                max_move = max(max_move, cnt+1)
                dfs(nx, ny, cnt+1)
                visited[nx][ny] = False  # x, y의 다른 nx, ny를 탐색할 때 영향을 끼치지 않기 위해
            else:
                print(-1)
                exit()


dfs(0, 0, 0)
print(max_move+1)
