import sys
from collections import deque

input = sys.stdin.readline

# 내 풀이
n = int(input())
k = int(input())


def answer():
    if k > n//2:
        return 0
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][1] = i
    for i in range(2, k + 1):
        for j in range(2*i, n+1):
            dp[j][i] = dp[j-2][i-1] + dp[j-1][i]
    return dp[n][k] % 1000000003


print(answer())

# 빠른 풀이
n = int(input())
k = int(input())

dp = [[-1] * (k+1) for _ in range(n+1)]
dp[0] = [0 for _ in range(k+1)]

for i in range(1, n+1):
    dp[i][1] = i


def func(n, k):
    if dp[n][k] != -1:
        return dp[n][k]
    elif k > n // 2:
        dp[n][k] = 0
    else:
        dp[n][k] = (func(n-2, k-1) + func(n-1, k)) % 1000000003
    return dp[n][k]


print(func(n, k))
