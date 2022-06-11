import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n, r, q = map(int, input().split())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (n+1)
child = [1] * (n+1)


def dfs(x):
    visited[x] = True
    child_num = 1
    for i in tree[x]:
        if visited[i] == False:
            child_num += dfs(i)
    child[x] = child_num
    return child_num


dfs(r)

for _ in range(q):
    root = int(input())
    print(child[root])
