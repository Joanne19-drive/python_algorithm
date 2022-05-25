import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

queue = deque()
dp = [-1] * 100_001
dp[n] = 100_001
queue.append([n, 0])

while queue:
    loc, cnt = queue.popleft()
    if loc == k:
        break
    else:
        if loc > 0 and dp[loc-1] == -1:
            dp[loc-1] = loc
            queue.append([loc-1, cnt+1])
        if loc < 100_000 and dp[loc+1] == -1:
            dp[loc+1] = loc
            queue.append([loc+1, cnt+1])
        if loc < 50_001 and dp[loc*2] == -1:
            dp[loc*2] = loc
            queue.append([loc*2, cnt+1])

print(cnt)
ans = []
while loc != 100_001:
    ans.append(loc)
    loc = dp[loc]

print(*ans[::-1])
