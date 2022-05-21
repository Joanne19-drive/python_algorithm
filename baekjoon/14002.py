import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

dp = [1] * n  # 각 자리까지 최장 수열의 길이
path = [-1] * n  # 각 자리별 최장 수열의 직전 경로

ans = 0  # 최종적으로 답이 될 최장수열이 끝나는 지점

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
            path[i] = j
    if dp[ans] < dp[i]:
        ans = i

print(dp[ans])

ans_arr = []
while ans != -1:
    ans_arr.insert(0, a[ans])
    ans = path[ans]

print(*ans_arr)
