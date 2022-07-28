import sys

input = sys.stdin.readline

# pypy3 제출
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

cnt = 0


def pushing(s):
    i, j, direction = s
    global cnt

    if i == n-1 and j == n-1:
        cnt += 1
        return

    if i + 1 < n and j + 1 < n:
        if house[i+1][j] == 0 and house[i][j+1] == 0 and house[i+1][j+1] == 0:
            pushing((i+1, j+1, 0))

    if direction == -1 or direction == 0:
        if j + 1 < n:  # 아래 코드를 and로 합치면 시간초과 남. 따로 써야 시간초과 안남.
            if house[i][j+1] == 0:
                pushing((i, j+1, -1))

    if direction == 0 or direction == 1:
        if i + 1 < n:
            if house[i+1][j] == 0:
                pushing((i+1, j, 1))


pushing((0, 1, -1))
print(cnt)
