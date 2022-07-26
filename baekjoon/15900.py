import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n+1)
cnt = 0


def dfs(i, turn):
    global cnt

    visited[i] = True

    flag = True
    for child in tree[i]:
        if not visited[child]:
            flag = False
            dfs(child, turn + 1)

    if flag:
        cnt += turn


dfs(1, 0)
print("Yes" if cnt % 2 == 1 else "No")
