import sys

input = sys.stdin.readline

n = int(input())

building = [[]]
time = [0] * (n+1)
visited = [False] * (n+1)

for k in range(n):
    t, *antecedent = list(map(int, input().split()))
    time[k+1] = t
    building.append(antecedent)


def dp(i):
    if visited[i]:
        return time[i]

    visited[i] = True
    ante_time = 0
    for ante in building[i]:
        if ante == -1:
            break
        ante_time = max(dp(ante), ante_time)

    time[i] += ante_time
    return time[i]


for i in range(1, n+1):
    print(dp(i))
