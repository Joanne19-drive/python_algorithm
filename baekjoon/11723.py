import sys

input = sys.stdin.readline

n = int(input())

S = 0b0


for _ in range(n):
    order = input().split()

    if order[0] == 'add':
        S |= (1 << int(order[1]))
    elif order[0] == 'remove':
        S &= ~(1 << int(order[1]))
    elif order[0] == 'check':
        print(1 if (S & (1 << int(order[1]))) > 0 else 0)
    elif order[0] == 'toggle':
        S ^= (1 << int(order[1]))
    elif order[0] == 'all':
        S = (1 << 21) - 1
    elif order[0] == 'empty':
        S = 0b0
