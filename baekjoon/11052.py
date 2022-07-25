import sys

input = sys.stdin.readline

# 풀이 1: 시간이 좀 더 걸리고 메모리 더 많이 사용
n = int(input())
p = [0] + list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-i] + p[i])

print(max(dp[n]))

# 풀이 2: 간 to the 단
n = int(input())
p = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + p[j])

print(dp[n])
