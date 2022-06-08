import sys

input = sys.stdin.readline
v, e = map(int, input().split())


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    parent[y] = x


# 최소신장트리(MST): Kruskal 알고리즘 이용
parent = [i for i in range(v+1)]
nodes = [list(map(int, input().split())) for _ in range(e)]

nodes.sort(key=lambda x: x[2])

ans = 0
node_cnt = 0

for a, b, c in nodes:
    if find(a) == find(b):
        continue
    union(a, b)
    ans += c
    node_cnt += 1
    if node_cnt == v-1:
        break

print(ans)
