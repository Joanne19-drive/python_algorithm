n = int(input())
time_slot = []
for _ in range(n):
    a, b = map(int, input().split())
    time_slot.append((a, b))
time_slot = sorted(time_slot, key=lambda x: (x[1], x[0]))
max_conf = []
for i in range(n):
    if i == 0:
        max_conf.append(time_slot[i])
    else:
        if time_slot[i][0] >= max_conf[-1][1]:
            max_conf.append(time_slot[i])
print(len(max_conf))
