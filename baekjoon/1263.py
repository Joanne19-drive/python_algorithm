import sys

input = sys.stdin.readline
n = int(input())

schedule = sorted([list(map(int, input().split()))
                  for _ in range(n)], key=lambda x: x[1], reverse=True)

# 시간 순이 아니라 시간 역순으로 파악을 해야 최대한 늦은 시작시간을 유추할 수 있다.
start_time = schedule[0][1] - schedule[0][0]
for i in range(1, n):
    if schedule[i][1] >= start_time:
        start_time -= schedule[i][0]
    else:
        start_time = schedule[i][1] - schedule[i][0]

print(start_time if start_time >= 0 else -1)
