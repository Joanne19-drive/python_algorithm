import sys

input = sys.stdin.readline

# pypy로 통과한 풀이.
# 매번 visited[i]가 0인지 아닌지 확인해야 했음.

n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxes = sorted(list(map(int, input().split())))
visited = [0] * m


def ship():
    if boxes[-1] > cranes[0]:
        return -1
    else:
        cnt = 0
        turn = 0

        while cnt < m:
            turn += 1
            j = 0
            for i in range(m-1, -1, -1):
                if j == n:
                    break
                if visited[i]:
                    continue
                if boxes[i] <= cranes[j]:
                    visited[i] = turn
                    j += 1
                    cnt += 1

        return turn


print(ship())


# 파이썬으로 통과한 풀이.
# 매 크레인마다 박스를 전부 돌면서 담을 수 있는지 확인하지 않고 담을 수 있는 무게부터 돌 수 있도록 starts_from에 저장.

n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)
visited = [0] * m

starts_from = [0] * n


def ship():
    if boxes[0] > cranes[0]:
        return -1
    cnt = 0
    turn = 0

    while cnt < m:
        turn += 1
        for i in range(n):
            while starts_from[i] < m:
                if not visited[starts_from[i]] and boxes[starts_from[i]] <= cranes[i]:
                    visited[starts_from[i]] = turn
                    starts_from[i] += 1
                    cnt += 1
                    break
                starts_from[i] += 1
    return turn


print(ship())
