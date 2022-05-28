import sys

input = sys.stdin.readline
INF = 1e9
n = int(input())
m = int(input())


def find_path(start, end):
    if path[start][end] == -1:
        return []
    k = path[start][end]
    return find_path(start, k) + [k+1] + find_path(k, end)


res = [[INF]*n for _ in range(n)]
path = [[-1]*n for _ in range(n)]
for i in range(n):
    res[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    res[a-1][b-1] = min(res[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if res[i][j] > res[i][k] + res[k][j]:
                res[i][j] = res[i][k] + res[k][j]
                path[i][j] = k  # i에서 j로 갈 때 중간에 들르는 곳 k를 저장

for i in range(n):
    for j in range(n):
        print(res[i][j] if res[i][j] != INF else 0, end=' ')
    print()

for i in range(n):
    for j in range(n):
        if res[i][j] in [0, INF]:
            print(0)
        else:
            min_cost_path = [i+1] + find_path(i, j) + [j+1]
            print(len(min_cost_path), end=" ")
            print(*min_cost_path)
