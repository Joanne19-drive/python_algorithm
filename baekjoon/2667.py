import sys

input = sys.stdin.readline
n = int(input())
apt = [input() for _ in range(n)]
visited = [[False] * n for _ in range(n)]
apt_group = [0]
total_group = 0


def dfs(a, b):
    if visited[a][b] == False:
        visited[a][b] = True
        if apt[a][b] == '1':
            apt_group[total_group] += 1
            if a > 0:
                dfs(a-1, b)
            if b > 0:
                dfs(a, b-1)
            if a < n-1:
                dfs(a+1, b)
            if b < n-1:
                dfs(a, b+1)


for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            if apt[i][j] == '1':
                apt_group.append(0)
                total_group += 1
                dfs(i, j)

apt_group.sort()

print(total_group)
for i in apt_group[1:]:
    print(i)
