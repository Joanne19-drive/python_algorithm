import sys
from collections import deque

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

# S에서 T를 만드는 건 시간초과 + 메모리초과.
# T에서 S를 만들 때는 T의 맨 끝자리에 따라 연산이 하나로 정해져있기 떄문에 보다 수월함.
flag = False

while len(T) > len(S):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1][::-1]
    if T == S:
        flag = True
        break

print(1 if flag else 0)
