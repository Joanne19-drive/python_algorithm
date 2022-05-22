import sys
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
temp = [arr[0]]

for i in range(1, n):
    num = arr[i]
    if num > temp[-1]:
        temp.append(num)
        dp[i] = len(temp)
    else:
        idx = bisect_left(temp, num)  # 이진탐색을 이용하여 arr[i]가 들어갈 만한 자리 찾기
        dp[i] = idx + 1
        temp[idx] = num

max_len = len(temp)

ans = []
for i in range(n-1, -1, -1):
    if dp[i] == max_len:
        ans.append(arr[i])
        max_len -= 1
    if max_len < 1:
        break
print(len(ans))
print(*ans[::-1])
