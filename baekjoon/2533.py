import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n+1)
dp = [[0, 1] for _ in range(n+1)]


def dfs(i):
    visited[i] = True
    for child in tree[i]:
        if not visited[child]:
            dfs(child)
            dp[i][0] += dp[child][1]
            dp[i][1] += min(dp[child][0], dp[child][1])


dfs(1)
print(min(dp[1]))
