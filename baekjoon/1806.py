import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, n):
    arr[i] += arr[i-1]

start = 0
end = 0

shortest = 100_001

while start < n and end < n:
    if start == 0:
        part_sum = arr[end]
    else:
        part_sum = arr[end] - arr[start-1]
    if part_sum >= s:
        shortest = min(shortest, end-start+1)
        start += 1
    else:
        end += 1

print(shortest if shortest != 100_001 else 0)
