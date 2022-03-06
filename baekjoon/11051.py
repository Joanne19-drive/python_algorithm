# 11050번과 풀이 동일
n, k = map(int, input().split())
t = 1
for i in range(n-k+1, n+1):
    t *= i
for j in range(1, k+1):
    t //= j
t %= 10007
print(t)
