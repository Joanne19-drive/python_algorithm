import sys
from math import inf

input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins = sorted(list(set(coins)))

n = len(coins)

dp = [[inf] * (k+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    coin = coins[i]
    for j in range(k+1):
        if j < coin:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j-coin]+1)

print(dp[n][k] if dp[n][k] != inf else -1)
