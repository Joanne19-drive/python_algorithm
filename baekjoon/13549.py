import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
q = deque()
q.append(n)
visited = [-1] * 100_001
visited[n] = 0

while q:
    loc = q.popleft()
    if loc == k:
        break
    # loc * 2가 loc + 1, loc - 1보다 먼저 실행되어야 함.
    # loc == 1일 때 loc + 1 도 2이고 loc * 2 도 2이기 때문에 loc * 2를 통해 가는 것이 더 빠르기 때문.
    if 0 <= loc*2 and loc*2 <= 100_000 and visited[loc*2] == -1:
        visited[loc*2] = visited[loc]
        q.append(loc*2)
    for i in [loc-1, loc+1]:
        if 0 <= i and i <= 100_000 and visited[i] == -1:
            visited[i] = visited[loc] + 1
            q.append(i)


print(visited[loc])
