import sys
from collections import deque

# 풀이 1 BFS 시간이 오래 걸림.
input = sys.stdin.readline
case = 1


def bfs(i):
    is_tree = True

    q = deque()
    q.append(i)

    while q:
        node = q.popleft()
        if visited[node] == True:
            is_tree = False
        visited[node] = True
        for child in tree[node]:
            if visited[child] == False:
                q.append(child)

    return is_tree


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    tree = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = [False] * (n+1)
    cnt = 0

    for i in range(1, n+1):
        if visited[i] == True:
            continue
        if bfs(i) == True:
            cnt += 1

    if cnt == 0:
        print(f'Case {case}: No trees.')
    elif cnt == 1:
        print(f'Case {case}: There is one tree.')
    elif cnt > 1:
        print(f'Case {case}: A forest of {cnt} trees.')

    case += 1

# 풀이 2 DFS 시간이 매우 짧게 걸림

input = sys.stdin.readline
case = 1


def dfs(parent, node):
    visited[node] = True
    for child in tree[node]:
        if child == parent:
            continue
        if visited[child]:
            return False
        if not dfs(node, child):
            return False
    return True


while True:
    n, m = map(int, input().split())
    if [n, m] == [0, 0]:
        break

    tree = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = [False] * (n+1)
    cnt = 0

    for i in range(1, n+1):
        if visited[i]:
            continue
        if dfs(0, i):
            cnt += 1

    if cnt == 0:
        print(f'Case {case}: No trees.')
    elif cnt == 1:
        print(f'Case {case}: There is one tree.')
    elif cnt > 1:
        print(f'Case {case}: A forest of {cnt} trees.')

    case += 1
