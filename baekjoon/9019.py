import sys
from collections import deque

input = sys.stdin.readline

# 풀이 1 : 짧은 코드, 긴 시간


def dslr_calculator(a, b):
    visited = [False] * 10000
    visited[a] = True

    q = deque()
    q.append([a, ''])

    while q:
        register, command = q.popleft()
        if register == b:
            return command
        next_reg = [(register * 2) % 10000, register - 1, register//1000 +
                    (register % 1000)*10, register//10 + (register % 10)*1000]
        c = ['D', 'S', 'L', 'R']
        for i in range(4):
            nr = next_reg[i]
            if nr == -1:
                nr = 9999
            if not visited[nr]:
                visited[nr] = True
                q.append([nr, command+c[i]])


T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    print(dslr_calculator(a, b))


# 풀이 2 : 짧은 시간, 긴 코드

def dslr_calculator(a, b):
    visited = [False] * 10000
    visited[a] = True

    q = deque()
    q.append([a, ''])

    while q:
        register, command = q.popleft()
        if register == b:
            return command
        reg1 = (register * 2) % 10000
        if not visited[reg1]:
            visited[reg1] = True
            q.append([reg1, command + 'D'])
        reg2 = register - 1
        if reg2 == -1:
            reg2 = 9999
        if not visited[reg2]:
            visited[reg2] = True
            q.append([reg2, command + 'S'])
        reg3 = register//1000 + (register % 1000)*10
        if not visited[reg3]:
            visited[reg3] = True
            q.append([reg3, command + 'L'])
        reg4 = register//10 + (register % 10)*1000
        if not visited[reg4]:
            visited[reg4] = True
            q.append([reg4, command + 'R'])


T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    print(dslr_calculator(a, b))
