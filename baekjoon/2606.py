import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0


def dfs(n):
    global count

    visited[n] = True
    for i in graph[n]:
        if visited[i] == False:
            count += 1
            dfs(i)


dfs(1)
print(count)
