import sys

# 풀이 1 | 메모리를 덜 쓰고 더 빠름
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(1, n):
        arr[i][j] += arr[i][j-1]
for i in range(1, n):
    for j in range(n):
        arr[i][j] += arr[i-1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 1 and y1 == 1:
        print(arr[x2-1][y2-1])
    elif x1 == 1:
        print(arr[x2-1][y2-1]-arr[x2-1][y1-2])
    elif y1 == 1:
        print(arr[x2-1][y2-1]-arr[x1-2][y2-1])
    else:
        print(arr[x2-1][y2-1]-arr[x1-2][y2-1]-arr[x2-1][y1-2]+arr[x1-2][y1-2])

# 풀이 2 | 길이가 짧고 상대적으로 알아보기 더 쉬움
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sum_list = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        sum_list[i+1][j+1] = sum_list[i+1][j] + arr[i][j]
for i in range(2, n+1):
    for j in range(1, n+1):
        sum_list[i][j] += sum_list[i-1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum_list[x2][y2]-sum_list[x1-1][y2] -
          sum_list[x2][y1-1]+sum_list[x1-1][y1-1])
