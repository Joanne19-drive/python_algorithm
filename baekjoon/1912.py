n = int(input())
arr = list(map(int, input().split()))
sum = [0] * n
for i in range(n):
    if i == 0:
        sum[i] = arr[i]
    else:
        sum[i] = max(sum[i-1]+arr[i], arr[i])
print(max(sum))
