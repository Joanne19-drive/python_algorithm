import sys
from collections import deque

input = sys.stdin.readline


def grouping(i):
    visited[i] = 1
    q = deque()
    q.append(i)
    while q:
        i = q.popleft()
        for num in graph[i]:
            if visited[num] == 0:
                visited[num] = 3 - visited[i]
                q.append(num)
            else:
                if visited[i] == visited[num]:
                    return False


def bipartite(v, e):
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 서로 연결되지 않은 부분이 있을 수 있기 때문에 1부터 연결하고 나서도 visited가 0인 애를 찾아야 함.
    for i in range(1, v+1):
        if visited[i] == 0:
            if grouping(i) == False:
                return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for k in range(v+1)]
    visited = [0 for k in range(v+1)]
    print(bipartite(v, e))
