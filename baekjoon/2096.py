import sys
from math import inf

input = sys.stdin.readline

n = int(input())

min_points = [[0] * 3 for _ in range(2)]
max_points = [[0] * 3 for _ in range(2)]

for turn in range(n):
    now = list(map(int, input().split()))
    min_points[0] = min_points[1][:]
    max_points[0] = max_points[1][:]
    min_points[1][0] = min(min_points[0][0], min_points[0][1]) + now[0]
    min_points[1][1] = min(
        min_points[0][0], min_points[0][1], min_points[0][2]) + now[1]
    min_points[1][2] = min(min_points[0][1], min_points[0][2]) + now[2]
    max_points[1][1] = max(
        max_points[0][0], max_points[0][1], max_points[0][2]) + now[1]
    max_points[1][2] = max(max_points[0][1], max_points[0][2]) + now[2]
    max_points[1][0] = max(max_points[0][0], max_points[0][1]) + now[0]

print(max(max_points[1]), min(min_points[1]))
