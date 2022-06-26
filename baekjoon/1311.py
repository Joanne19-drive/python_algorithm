import sys

input = sys.stdin.readline
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [10**6] * (1 << n)


def dfs(row, visit):
    if row == n:
        return 0

    if dp[visit] < 10 ** 6:
        return dp[visit]

    for i in range(n):
        if visit & (1 << i) > 0:
            continue
        dp[visit] = min(dp[visit], dfs(
            row + 1, visit | (1 << i)) + cost[row][i])

    return dp[visit]


print(dfs(0, 0))
