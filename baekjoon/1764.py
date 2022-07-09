import sys

input = sys.stdin.readline

n, m = map(int, input().split())
no_heard = sorted([input().rstrip() for _ in range(n)])
no_seen = sorted([input().rstrip() for _ in range(m)])
i, j = 0, 0

result = []

while i < n and j < m:
    if no_heard[i] < no_seen[j]:
        i += 1
    elif no_heard[i] == no_seen[j]:
        result.append(no_heard[i])
        i += 1
    else:
        j += 1

print(len(result))
for name in result:
    print(name)
