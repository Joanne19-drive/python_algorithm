import sys

k, n = map(int, sys.stdin.readline().split())
line = [int(sys.stdin.readline()) for _ in range(k)]

start, end = 1, max(line)
result = 0
while end >= start:
    mid = (start+end)//2
    count = 0
    for i in line:
        count += i//mid
    if count < n:
        end = mid - 1
    if count >= n:
        start = mid + 1
        result = mid

print(result)
