import sys

# pypy로 제출해야 시간초과가 안나는 풀이
# 플로이드 워셜 알고리즘 사용
input = sys.stdin.readline
INF = 1e9
v, e = map(int, input().split())

distance = [[INF] * v for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, input().split())
    distance[a-1][b-1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            distance[i][j] = min(
                distance[i][j], distance[i][k] + distance[k][j])

min_cycle = INF
for i in range(v):
    min_cycle = min(min_cycle, distance[i][i])

print(min_cycle if min_cycle != INF else -1)

# heapq를 사용해서 python3으로도 시간초과 없이 풀 수 있는 방법이 있던데 시간 나면 시도해볼 것.
