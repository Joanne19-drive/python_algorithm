import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    candidates = [list(map(int, input().split())) for i in range(n)]

    candidates.sort()

    cut = 0
    cnt = 1

    for i in range(1, n):
        if candidates[cut][1] > candidates[i][1]:
            cut = i
            cnt += 1

    print(cnt)
