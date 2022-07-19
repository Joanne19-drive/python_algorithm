import sys

input = sys.stdin.readline

n = int(input())
children = [int(input()) for _ in range(n)]

# 가장 긴 증가하는 부분 수열을 활용하는 문제
dp = [1] * n

ans = 0

for i in range(1, n):
    for j in range(i):
        if children[i] > children[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
    if dp[ans] < dp[i]:
        ans = i

print(n - dp[ans])
