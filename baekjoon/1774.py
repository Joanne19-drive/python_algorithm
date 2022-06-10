import sys
input = sys.stdin.readline
n, m = map(int, input().split())

gods = [tuple(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n)]

dst = []


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    parent[y] = x


for _ in range(m):
    x, y = map(int, input().split())
    union(x-1, y-1)

for i in range(n-1):
    for j in range(i+1, n):
        if find(i) == find(j):
            continue
        distance = ((gods[i][0] - gods[j][0]) ** 2 +
                    (gods[i][1] - gods[j][1]) ** 2) ** 0.5
        dst.append((i, j, distance))

dst.sort(key=lambda x: x[2])

ans = 0

for x, y, distance in dst:
    if find(x) == find(y):
        continue
    union(x, y)
    ans += distance

print(f'{ans:.2f}')
