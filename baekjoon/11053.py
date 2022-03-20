import sys

n = int(sys.stdin.readline())
arr = list(map(int, input().split()))
max_len = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            max_len[i] = max(max_len[i], max_len[j]+1)
print(max(max_len))
