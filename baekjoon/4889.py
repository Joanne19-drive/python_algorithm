import sys
from collections import deque

input = sys.stdin.readline

# 풀이 1

S = list(input().rstrip())
cnt = 1

while '-' not in S:
    stack = 0
    min_cal = 0
    for s in S:
        if s == '}':
            if not stack:
                min_cal += 1
                stack += 1
            else:
                stack -= 1
        else:
            stack += 1
    min_cal += stack//2
    print(str(cnt)+'.', min_cal)
    cnt += 1
    S = list(input().rstrip())

# 풀이 2

S = list(input().rstrip())
cnt = 1

while '-' not in S:
    stack = deque()
    for s in S:
        if s == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)

    min_cal = 0
    for i in range(0, len(stack), 2):
        if stack[i] == stack[i+1]:
            min_cal += 1
        else:
            min_cal += 2
    print(str(cnt)+'.', min_cal)
    cnt += 1
    S = list(input().rstrip())
