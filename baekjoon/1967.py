import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])


def bfs(i):
    visited = [False] * (n+1)
    farthest = [i, 0]
    q = deque()
    q.append([i, 0])

    while q:
        node, dist = q.popleft()
        visited[node] = True
        if dist > farthest[1]:
            farthest = [node, dist]
        for child, d in tree[node]:
            if not visited[child]:
                q.append([child, dist + d])
    return farthest


# 1에서 가장 먼 노드 start 찾기
start, dist1 = bfs(1)
# start에서 가장 먼 노드 end와 end까지의 길이 찾기
end, result = bfs(start)

print(result)
