import sys
from collections import deque

input = sys.stdin.readline
dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

# 이걸 for문 안에 넣는 대신 함수화 하는 것이 훨씬 시간 절약


def bfs(i, x, y, w, z):
    board = [[0] * i for k in range(i)]
    board[x][y] = 1
    q = deque()
    q.append([x, y])
    while q:
        chess = q.popleft()
        a, b = chess[0], chess[1]
        if a == w and b == z:
            return board[a][b]-1
        for j in range(8):
            abjx, abjy = a + dx[j], b + dy[j]
            if 0 <= abjx < i and 0 <= abjy < i and board[abjx][abjy] == 0:
                board[abjx][abjy] = board[a][b] + 1
                q.append([abjx, abjy])


t = int(input())
for _ in range(t):
    i = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    print(bfs(i, start_x, start_y, end_x, end_y))
