import sys

input = sys.stdin.readline
INF = 1e9
n, m = map(int, input().split())
route = [list(map(int, input().split())) for _ in range(m)]

track = [INF] * (n+1)
track[1] = 0

# 벨만-포드 알고리즘 | 음의 간선이 있을 때 사용
for _ in range(n-1):
    for a, b, c in route:
        if track[a] != INF and track[a] + c < track[b]:
            track[b] = track[a] + c

cycle = False
for a, b, c in route:
    if track[a] != INF and track[a] + c < track[b]:
        cycle = True
        print(-1)
        break

if cycle == False:
    for i in range(2, n+1):
        print(track[i] if track[i] != INF else -1)
