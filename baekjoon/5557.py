import sys

input = sys.stdin.readline
n = int(input())
num_list = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n-1)]
dp[0][num_list[0]] = 1

for i in range(0, n-2):
    for j in range(21):
        if dp[i][j] > 0:
            cal_nums = [j + num_list[i+1], j - num_list[i+1]]
            for num in cal_nums:
                if 0 <= num <= 20:
                    dp[i+1][num] += dp[i][j]


print(dp[n-2][num_list[-1]])
