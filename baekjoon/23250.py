import sys

input = sys.stdin.readline

N, K = map(int, input().split())

f, t = 1, 3

while True:
    if K < 2 ** (N-1):
        N -= 1
        t = 6 - f - t
    elif K > 2 ** (N-1):
        K -= (2 ** (N-1))
        N -= 1
        f = 6 - f - t
    else:
        print(f, t)
        break
