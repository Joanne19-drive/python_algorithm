import sys

input = sys.stdin.readline

n, c = map(int, input().split())
iptime = [int(input()) for _ in range(n)]
iptime.sort()

start, end = 1, iptime[-1] - iptime[0]
mid = (iptime[0] + iptime[-1]) // 2

while end >= start:
    spot = 1
    datum = iptime[0]
    for k in iptime:
        if k - datum >= mid:
            datum = k
            spot += 1

    if spot >= c:
        start = mid + 1
    else:
        end = mid - 1
    mid = (start + end) // 2

print(end)
