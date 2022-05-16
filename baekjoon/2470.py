import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, n-1
least_gap = 2000000001
pair = None

while start < end:
    gap = arr[start] + arr[end]
    if abs(gap) < least_gap:
        least_gap = abs(gap)
        pair = (arr[start], arr[end])
        if least_gap == 0:
            break
    if gap < 0:
        start += 1
        continue
    end -= 1

print(*pair)
