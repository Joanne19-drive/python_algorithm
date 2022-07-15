import sys

input = sys.stdin.readline

k = int(input())
line = [list(map(int, input().split())) for _ in range(6)]

max_width = max([x[1] for x in line if x[0] in [1, 2]])
max_length = max([x[1] for x in line if x[0] in [3, 4]])

v = []

for i in range(6):
    if line[i][1] == max_width or line[i][1] == max_length:
        v.append(i)

total = line[v[0]][1] * line[v[1]][1] - \
    line[(v[0] + 3) % 6][1] * line[(v[1] + 3) % 6][1]
print(total * k)
