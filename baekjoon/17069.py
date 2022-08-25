import sys

input = sys.stdin.readline

# 내 풀이
N = int(input())
new_house = [list(map(int, input().split())) for _ in range(N)]

p = [[[0, 0, 0] for i in range(N)] for _ in range(N)]
p[0][1] = [1, 0, 1]

for i in range(N):
    for j in range(2, N):
        if new_house[i][j] == 1:
            continue
        if 0 <= i-1 and new_house[i-1][j] == 0:
            p[i][j][1] += p[i-1][j][1]
            p[i][j][2] += p[i-1][j][1]
            if new_house[i-1][j-1] == 0 and new_house[i][j-1] == 0:
                p[i][j][0] += p[i-1][j-1][2]
                p[i][j][1] += p[i-1][j-1][2]
                p[i][j][2] += p[i-1][j-1][2]
        if new_house[i][j-1] == 0:
            p[i][j][0] += p[i][j-1][0]
            p[i][j][2] += p[i][j-1][0]

print(max(p[N-1][N-1]))

# 더 짧은 풀이
N = int(input())
new_house = [list(map(int, input().split())) for _ in range(N)]

p = [[[0, 0, 0] for i in range(N)] for _ in range(N)]
for i in range(1, N):
    if new_house[0][i] == 1:
        break
    p[0][i][0] = 1

for i in range(1, N):
    for j in range(2, N):
        if new_house[i][j]:
            continue
        p[i][j][0] = p[i][j-1][0] + p[i][j-1][2]
        p[i][j][1] = p[i-1][j][1] + p[i-1][j][2]
        if new_house[i-1][j] == new_house[i][j-1] == 0:
            p[i][j][2] = sum(p[i-1][j-1])

print(sum(p[N-1][N-1]))
