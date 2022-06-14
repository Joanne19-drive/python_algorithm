import sys

input = sys.stdin.readline
n = int(input())

w = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


dp = [[0, 0] for _ in range(n+1)]
max_set = [[[], []] for _ in range(n+1)]
visited = [False] * (n+1)


def dfs(i):
    visited[i] = True
    dp[i][1] = w[i]
    dp[i][0] = 0
    max_set[i][1] = [i]

    for child in tree[i]:
        if not visited[child]:
            dfs(child)
            dp[i][1] += dp[child][0]
            max_set[i][1] += max_set[child][0]
            if dp[child][0] < dp[child][1]:
                dp[i][0] += dp[child][1]
                max_set[i][0] += max_set[child][1]
            else:
                dp[i][0] += dp[child][0]
                max_set[i][0] += max_set[child][0]


dfs(1)

if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    print(*sorted(max_set[1][0]))
else:
    print(dp[1][1])
    print(*sorted(max_set[1][1]))
