import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
n, m = map(int, input().split())

root = [i for i in range(n+1)]


def find(x):
    if root[x] == x:
        return x
    p = find(root[x])  # 여기서 바로 find(root[x]) 값을 리턴하는 대신
    root[x] = p  # root[x]의 값을 p로 바꿔놓으면 나중에 다시 find(x)를 할 떄의 시간을 줄이게 됨.
    return p  # x와 루트 노드 값 사이의 값들은 이 문제에서 필요가 없기 때문에 노프라블럼.


def union(x, y):
    x = find(x)
    y = find(y)

    root[y] = x


for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):  # 루트 노드 값이 동일하다 == 같은 집합에 있다
            print("YES")
        else:
            print("NO")
