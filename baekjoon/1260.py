import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
tree = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for node in tree:
    node.sort()


def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in tree[n]:
        if visited[i] == False:
            dfs(i)


def bfs(n):
    visited[n] = True
    queue = deque([n])
    while queue:
        next_num = queue.popleft()
        print(next_num, end=' ')
        for i in tree[next_num]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

    pass


visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
