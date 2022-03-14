import sys
sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (n+1)


def DFS(p):
    global tree, parent
    for i in tree[p]:
        if parent[i] == 0:
            parent[i] = p
            DFS(i)


DFS(1)
for node in parent[2:]:
    print(node)
