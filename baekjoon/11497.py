import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    log_height = sorted(list(map(int, input().split())))
    max_gap = 0
    for i in range(2, N):
        max_gap = max(max_gap, log_height[i]-log_height[i-2])
    print(max_gap)
