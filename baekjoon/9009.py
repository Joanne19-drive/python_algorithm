import sys

input = sys.stdin.readline

fib = [0, 1]

t = int(input())
for _ in range(t):
    n = int(input())
    while fib[-1] < n:
        fib.append(fib[-2] + fib[-1])
    ans = []
    k = len(fib) - 1
    while n > 0 and k >= 0:
        if n >= fib[k]:
            ans.append(fib[k])
            n -= fib[k]
        k -= 1
    print(*ans[::-1])
