n = int(input())
line = {}
for _ in range(n):
    a, b = map(int, input().split())
    line[a] = b

line = [li[1] for li in sorted(line.items())]
lcs = [1] * n
for i in range(n):
    for j in range(i):
        if line[j] < line[i]:
            lcs[i] = max(lcs[i], lcs[j]+1)
print(n-max(lcs))
