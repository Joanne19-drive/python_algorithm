import sys

input = sys.stdin.readline
n = int(input())

planets = [list(map(int, input().split())) + [i] for i in range(n)]

parent = [i for i in range(n)]

dst = []
cnt = 0


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    parent[y] = x


for i in range(3):
    planets.sort(key=lambda x: x[i])
    for j in range(n-1):
        if planets[j][i] == planets[j+1][i] and parent[planets[j][3]] != parent[planets[j+1][3]]:
            union(planets[j][3], planets[j+1][3])
            cnt += 1
        else:
            dst.append([abs(planets[j][i] - planets[j+1][i]),
                       planets[j][3], planets[j+1][3]])

dst.sort()
ans = 0

for distance, i, j in dst:
    if find(i) == find(j):
        continue
    union(i, j)
    cnt += 1
    ans += distance
    if cnt == n-1:
        break

print(ans)
