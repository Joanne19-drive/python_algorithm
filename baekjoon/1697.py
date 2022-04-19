import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())


def bfs():
    q = deque()
    visited = [0] * 100_001
    q.append(n)

    while q:
        loc = q.popleft()
        if loc == k:  # 처음부터 n == k일 때 0을 출력해버릴 수 있음. for 구문 아래에 이걸 넣으면 0 출력이 안됨.
            return visited[loc]

        for i in [loc-1, loc+1, loc*2]:
            if 0 <= i and i <= 100_000 and visited[i] == 0:
                visited[i] = visited[loc] + 1
                q.append(i)


print(bfs())
