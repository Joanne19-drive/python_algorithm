import sys
from collections import deque

input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
visited = [0] * (n+1)

q.append(r)
count = 1
visited[r] = count

while q:
    a = q.popleft()
    graph[a].sort()
    for i in graph[a]:
        if visited[i] == 0:
            count += 1
            visited[i] = count
            q.append(i)

for k in range(1, n+1):
    print(visited[k])
