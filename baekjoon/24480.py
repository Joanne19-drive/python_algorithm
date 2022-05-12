import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1


def dfs(r):
    global count

    visited[r] = count
    graph[r].sort(reverse=True)
    for i in graph[r]:
        if visited[i] == 0:
            count += 1
            dfs(i)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(r)
print(*visited[1:])
