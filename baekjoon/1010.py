t = int(input())
for _ in range(t):
    k, n = map(int, input().split())
    m = 1
    for i in range(n-k+1, n+1):
        m *= i
    for j in range(1, k+1):
        m //= j
    print(m)
