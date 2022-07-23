import sys

input = sys.stdin.readline
n = int(input())

work = [0] * (n+1)
antecedent = [[] for _ in range(n+1)]

for i in range(1, n+1):
    time, former, *antecedents = map(int, input().split())
    work[i] = time
    if former:
        antecedent[i] = antecedents

visited = [False] * (n+1)


def dp(i):
    if visited[i]:
        return work[i]

    visited[i] = True

    if antecedent[i] == []:
        return work[i]

    work[i] += max([dp(x) for x in antecedent[i]])
    return work[i]


for i in range(1, n+1):
    if not visited[i]:
        dp(i)

print(max(work))
