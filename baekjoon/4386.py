import sys

input = sys.stdin.readline
n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]

dst = []
parent = [i for i in range(n)]

for i in range(n-1):
    for j in range(i+1, n):
        distance = ((stars[i][0] - stars[j][0]) ** 2 +
                    (stars[i][1] - stars[j][1]) ** 2) ** 0.5
        dst.append((i, j, distance))

dst.sort(key=lambda x: x[2])


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    parent[y] = x


ans = 0

for a, b, c in dst:
    if find(a) == find(b):
        continue
    union(a, b)
    ans += c

print(f'{ans:.2f}')
