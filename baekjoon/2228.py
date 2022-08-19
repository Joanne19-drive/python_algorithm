import sys

input = sys.stdin.readline

N, M = map(int, input().split())
array = [0] + [int(input()) for _ in range(N)]

dp = [[0] * (N+1) for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(i*2-1, N+1):
        if i == 1:
            dp[i][j] = max(array[j], dp[i][j-1] + array[j])
        elif j == i * 2 - 1:
            dp[i][j] = dp[i-1][j-2] + array[j]
        else:
            max_num = max(dp[i-1][i*2-3:j-1])
            dp[i][j] = max(max_num, dp[i][j-1]) + array[j]

print(max(dp[M][2*M-1:]))
