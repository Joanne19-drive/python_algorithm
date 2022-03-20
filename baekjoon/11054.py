n = int(input())
arr = list(map(int, input().split()))
left = [1] * n
right = [0] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            left[i] = max(left[i], left[j]+1)

for a in reversed(range(n)):
    for b in reversed(range(a+1, n)):
        if arr[b] < arr[a]:
            right[a] = max(right[a], right[b]+1)

total = [left[c] + right[c] for c in range(n)]
print(max(total))
