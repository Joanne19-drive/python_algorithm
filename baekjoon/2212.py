import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
loc = sorted(list(map(int, input().split())))

gap = []
for i in range(n-1):
    gap.append(loc[i+1]-loc[i])

gap.sort(reverse=True)
print(sum(gap[k-1:]))
