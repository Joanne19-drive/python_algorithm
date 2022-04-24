import sys

input = sys.stdin.readline
n, k = map(int, input().split())
temp = list(map(int, input().split()))
sot = [0]  # sum_of_temperature
for i in range(n):
    sot.append(temp[i]+sot[i])
fmt = [sot[i]-sot[i-k] for i in range(k, n+1)]  # find_max_temperature

print(max(fmt))
