import sys
from math import inf as INF

input = sys.stdin.readline

n = int(input())

rgb_road = [list(map(int, input().split())) for _ in range(n)]
ans = INF

for i in range(3):
    rgb_track = [[INF, INF, INF] for _ in range(n)]
    rgb_track[0][i] = rgb_road[0][i]
    for k in range(1, n):
        rgb_track[k][0] = min(
            rgb_track[k-1][1], rgb_track[k-1][2]) + rgb_road[k][0]
        rgb_track[k][1] = min(
            rgb_track[k-1][0], rgb_track[k-1][2]) + rgb_road[k][1]
        rgb_track[k][2] = min(
            rgb_track[k-1][0], rgb_track[k-1][1]) + rgb_road[k][2]

    for j in range(3):
        if i != j:
            ans = min(ans, rgb_track[n-1][j])

print(ans)
