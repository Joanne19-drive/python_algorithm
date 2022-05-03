import sys

input = sys.stdin.readline
INF = 1e9

n = int(input())
m = int(input())

cost = [[INF]*(n) for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

for i in range(n):
    cost[i][i] = 0

# 첫번째 for loop는 중간에 거치는 지점을 기준으로 함.
for j in range(n):
    for i in range(n):
        for k in range(n):
            cost[i][k] = min(cost[i][k], cost[i][j] + cost[j][k])

for li in cost:
    for i in range(n):
        if li[i] == INF:
            li[i] = 0
    print(*li)
