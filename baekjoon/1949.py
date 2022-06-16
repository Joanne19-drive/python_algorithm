import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
residents = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)


def dfs(i):
    visited[i] = True
    dp[i][1] = residents[i]
    for child in tree[i]:
        if not visited[child]:
            dfs(child)
            dp[i][0] += max(dp[child][1], dp[child][0])
            dp[i][1] += dp[child][0]


dfs(1)
print(max(dp[1]))
