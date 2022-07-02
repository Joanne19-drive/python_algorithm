import sys

input = sys.stdin.readline
t = int(input())

# 내 풀이
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m+1)

    for i in range(n):
        for j in range(1, m+1):
            if j == coins[i]:
                dp[j] += 1
            if dp[j] > 0 and j + coins[i] <= m:
                dp[j + coins[i]] += dp[j]

    print(dp[m])


# 효율적 풀이
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m+1)
    dp[0] = 1

    for coin in coins:
        for i in range(m+1):
            if i >= coin:
                dp[i] += dp[i-coin]

    print(dp[m])
