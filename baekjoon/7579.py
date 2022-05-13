import sys

input = sys.stdin.readline

# 내가 푼 방식
n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
ans = sum(cost)

# 열을 각 앱, 행을 m까지의 메모리 크기로 했었는데 시간초과 남. 행을 최대 비용까지의 비용 크기로 바꾸면 계산을 덜함.
dp = [[0] * (sum(cost)+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, sum(cost)+1):
        if cost[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]] + memory[i-1])
        else:
            dp[i][j] = dp[i-1][j]
        if dp[i][j] >= m:
            ans = min(ans, j)

print(ans)


# 특이한 풀이
n, m = map(int, input().split())
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))
li = [0] * (n*100+1)
costs = [0]
ans = sys.maxsize

for i in range(n):
    mm, c = mem[i], cost[i]
    l = len(costs)
    for jj in range(l-1, -1, -1):
        j = costs[jj]
        if c+j >= ans:
            continue

        if li[c+j] == 0:
            costs.append(c+j)
        li[c+j] = max(li[c+j], mm+li[j])
        if li[c+j] >= m:
            ans = min(ans, c+j)
    if len(costs) > l:
        costs.sort()

print(ans)
