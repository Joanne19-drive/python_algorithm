import sys
from collections import deque

input = sys.stdin.readline

# 그나마 제일 나았던 풀이
n, m = map(int, input().split())

board = [i for i in range(101)]
for _ in range(n+m):
    a, b = map(int, input().split())
    board[a] = b

visited = [0] * 101


def bfs():
    q = deque([1])

    while q:
        now = q.popleft()

        for i in range(1, 7):
            new_dest = now + i

            if new_dest > 100:
                continue

            new_dest = board[now+i]

            if visited[new_dest] == 0:
                visited[new_dest] = visited[now] + 1
                q.append(new_dest)

                if new_dest == 100:
                    return


bfs()
print(visited[100])

# 딕셔너리 사용한 풀이. 시간도 메모리도 와장창.
n, m = map(int, input().split())

jumping = {}
for _ in range(n+m):
    a, b = map(int, input().split())
    jumping[a] = b

visited = [False] * 101


def bfs():
    q = deque()
    q.append([1, 0])

    while q:
        now, cnt = q.popleft()
        visited[now] = True

        for i in range(1, 7):
            new_dest = now + i
            if new_dest in jumping:
                new_dest = jumping[new_dest]
            if new_dest >= 100:
                return cnt + 1
            elif not visited[new_dest]:
                q.append([new_dest, cnt+1])


print(bfs())
