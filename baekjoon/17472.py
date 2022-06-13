# 코드가 길지는 않지만 시간이 다른 사람들과 비교했을 때 2배가 걸림.
# 어떻게 시간을 줄일 수 있는지 고민을 해보쟈....

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cnt = 2

# dfs를 이용하여 각 섬을 labeling


def allocating(x, y, num):
    city_map[x][y] = num
    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m and city_map[next_x][next_y] == 1:
            allocating(next_x, next_y, num)


for x in range(n):
    for y in range(m):
        if city_map[x][y] == 1:
            allocating(x, y, cnt)
            cnt += 1

dst = []

# 행 탐색과 열 탐색의 코드가 중복되어서 이를 효율적으로 줄일 수 있는 함수를 만드는 것이 필요함.

# 행 탐색
for i in range(n):
    start = 0
    count = 0
    for j in range(m):
        if city_map[i][j] != 0 and start == 0:
            start = city_map[i][j]
        elif city_map[i][j] != 0 and start != city_map[i][j]:
            if count >= 2:
                dst.append([start, city_map[i][j], count])
            start = city_map[i][j]
            count = 0
        elif city_map[i][j] == 0 and start != 0:
            count += 1
        # ㄷ자 땅을 고려해서 같은 번호가 다시 나왔을 때 count를 0으로 돌려야 함.
        elif start == city_map[i][j]:
            count = 0

# 열 탐색
for j in range(m):
    start = 0
    count = 0
    for i in range(n):
        if city_map[i][j] != 0 and start == 0:
            start = city_map[i][j]
        elif city_map[i][j] != 0 and start != city_map[i][j]:
            if count >= 2:
                dst.append([start, city_map[i][j], count])
            start = city_map[i][j]
            count = 0
        elif city_map[i][j] == 0 and start != 0:
            count += 1
        elif start == city_map[i][j]:
            count = 0

dst.sort(key=lambda x: x[2])

parent = [i for i in range(cnt)]

lines = 0
min_length = 0


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    parent[y] = x


for a, b, length in dst:
    if find(a) == find(b):
        continue
    union(a, b)
    min_length += length
    lines += 1
    if lines == cnt-3:
        break

print(min_length if lines == cnt-3 else -1)
