import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    array = sys.stdin.readline().strip()[1: -1].split(',')
    array = [] if n == 0 else deque(array)
    reverse_deque = 0
    blank_possible = True  # 빈 array를 출력해야 할 상황을 위해
    for order in p:
        if order == "R":
            reverse_deque += 1
        elif order == "D":
            if array:
                if reverse_deque % 2 == 0:
                    array.popleft()
                else:
                    array.pop()
            else:
                blank_possible = False
                break
    if blank_possible == True:
        if reverse_deque % 2 == 1:
            array.reverse()
        print('[' + ','.join(array) + ']')
    else:
        print("error")
