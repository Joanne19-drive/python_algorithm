import sys

input = sys.stdin.readline
t = int(input())


def dp(n, arr):
    acc_sum = [0]
    for i in range(n):
        acc_sum.append(acc_sum[i]+arr[i])

    result = [[0]*(n+1) for i in range(n+1)]
    for j in range(2, n+1):
        for i in range(j-1, 0, -1):
            result[i][j] = min(result[i][k]+result[k+1][j]
                               for k in range(i, j)) + acc_sum[j] - acc_sum[i-1]

    return result[1][-1]


for _ in range(t):
    n = int(input())
    book = list(map(int, input().split()))
    print(dp(n, book))
