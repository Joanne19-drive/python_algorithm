import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

parent = [i for i in range(n)]
cnt = 0


def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])
    parent[x] = p
    return p


def union(x, y):
    global cnt
    x = find(x)
    y = find(y)
    if x == y and cnt == 0:
        cnt = i
        return
    parent[y] = x


for i in range(1, m+1):
    a, b = map(int, input().split())
    if cnt == 0:
        union(a, b)
print(cnt)
