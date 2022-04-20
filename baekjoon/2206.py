import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
maze = [[int(i) for i in input().rstrip()] for _ in range(n)]
visited = [[[0, 0] for a in range(m)] for b in range(n)]
visited[0][0][0] = 2

next = [[0, -1], [0, 1], [1, 0], [-1, 0]]


def bfs():
    q = deque()
    q.append([0, 0, 0])

    while q:
        point = q.popleft()
        x, y, z = point[0], point[1], point[2]
        for i in range(4):
            next_x = x + next[i][0]
            next_y = y + next[i][1]
            if 0 <= next_x < n and 0 <= next_y < m:
                if maze[next_x][next_y] == 1:
                    next_z = z + 1
                else:
                    next_z = z
                if next_z in [0, 1] and visited[next_x][next_y][next_z] == 0:
                    visited[next_x][next_y][next_z] = visited[x][y][z] + 1
                    q.append([next_x, next_y, next_z])

    if 0 in visited[n-1][m-1]:
        return max(visited[n-1][m-1]) - 1
    else:
        return min(visited[n-1][m-1]) - 1


print(bfs())
