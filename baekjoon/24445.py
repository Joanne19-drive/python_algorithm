from collections import deque
import sys
from queue import Queue

# 학교에서 배운 queue 모듈을 활용해본 풀이. 시간이 너무 오래 걸린다.
input = sys.stdin.readline

n, m, r = map(int, input().split())
tree = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = Queue()

q.put(r)
visited[r] = 1
cnt = 2

while not q.empty():
    node = q.get()
    tree[node].sort(reverse=True)

    for child in tree[node]:
        if not visited[child]:
            visited[child] = cnt
            cnt += 1
            q.put(child)

for i in visited[1:]:
    print(i)


# 기존에 deque를 queue처럼 썼던 걸 활용. 시간이 훨씬 빠르다.

n, m, r = map(int, input().split())
tree = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque()

q.append(r)
visited[r] = 1
cnt = 2

while q:
    node = q.popleft()
    tree[node].sort(reverse=True)

    for child in tree[node]:
        if not visited[child]:
            visited[child] = cnt
            cnt += 1
            q.append(child)

for i in visited[1:]:
    print(i)
