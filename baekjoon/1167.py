import sys
from collections import deque

input = sys.stdin.readline
v = int(input())

tree = [[] for _ in range(v+1)]
for _ in range(v):
    node = list(map(int, input().split()))
    i = node[0]
    for j in range(1, len(node)-1, 2):
        tree[i].append([node[j], node[j+1]])


def bfs(i):
    q = deque()
    q.append([i, 0])

    visited = [False] * (v+1)
    farthest = [i, 0]

    while q:
        node, dist = q.popleft()
        visited[node] = True
        if farthest[1] < dist:
            farthest = [node, dist]
        for child, distance in tree[node]:
            if not visited[child]:
                q.append([child, dist + distance])
    return farthest


start, d = bfs(i)
end, result = bfs(start)

print(result)
