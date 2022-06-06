import sys

input = sys.stdin.readline
t = int(input())


def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])
    parent[x] = p
    return p


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = parent[x]
        relation[x] += relation[y]


for _ in range(t):
    f = int(input())
    parent = dict()
    relation = dict()

    for r in range(f):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            relation[a] = 1
        if b not in parent:
            parent[b] = b
            relation[b] = 1

        union(a, b)
        print(relation[find(a)])
