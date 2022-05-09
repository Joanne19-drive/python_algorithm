import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

v, e, s = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [0] * (v+1)
visited[s] = 1
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
count = 1


def dfs(s):
    global count, graph
    graph[s] = sorted(graph[s])
    for i in graph[s]:
        if visited[i] == 0:
            count += 1
            visited[i] = count
            dfs(i)
        else:
            continue


dfs(s)
for i in range(1, v+1):
    print(visited[i])
