import sys

input = sys.stdin.readline

G = int(input())
P = int(input())
plane = [int(input()) for _ in range(P)]

# root[i]는 plane이 1~i 게이트 중 하나에 가고 싶을 때 도킹할 수 있는 가장 큰 수의 게이트
root = [i for i in range(G+1)]

# for문을 돌려가며 도킹 가능한 게이트를 찾으면 시간초과가 나기 때문에 union-find를 활용


def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        root[x] = y
    else:
        root[y] = x


cnt = 0

for p in plane:
    gate = find(p)
    if gate == 0:
        break
    # gate에 도킹이 가능할 때(gate가 0보다 클 때) gate 다음으로 도킹 가능한 번호의 게이트를 root에 저장
    union(gate, gate-1)
    cnt += 1

print(cnt)
