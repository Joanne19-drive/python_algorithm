import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
m = int(input())

parent = [i for i in range(n)]


def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])
    parent[x] = p
    return p


def union(x, y):
    x = find(x)
    y = find(y)

    parent[y] = x


for i in range(n):
    nodes = list(map(int, input().split()))
    for j in range(n):
        if nodes[j] == 1:
            union(i, j)

trip_plan = list(map(int, input().split()))
is_possible = True
root = parent[trip_plan[0]-1]

for t in trip_plan:
    if find(t-1) != root:
        is_possible = False
        break

print("YES" if is_possible else "NO")
