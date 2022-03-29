import sys
n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m, k = map(int, sys.stdin.readline().split())
b = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

sum_list = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        sum = 0
        for p in range(m):
            sum += a[i][p]*b[p][j]
        sum_list[i][j] = sum

for q in sum_list:
    print(*q)
