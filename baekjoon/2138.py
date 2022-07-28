import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().rstrip()))
B = list(map(int, input().rstrip()))


def greedy(A):
    cnt = 0
    for i in range(1, n-1):
        if A[i-1] != B[i-1]:
            cnt += 1
            A[i-1], A[i], A[i + 1] = not A[i-1], not A[i], not A[i+1]
    if A[n-2] != B[n-2]:
        cnt += 1
        A[n-2], A[n - 1] = not A[n-2], not A[n-1]
    if A[n-1] == B[n-1]:
        return cnt
    else:
        return -1


def answer():
    if A == B:
        return 0

    A1 = A[:]
    first_case = greedy(A1)
    A2 = A[:]
    A2[0], A2[1] = not A2[0], not A2[1]
    second_case = greedy(A2)

    if -1 not in [first_case, second_case]:
        return min(first_case, second_case+1)
    elif first_case == -1 and second_case == -1:
        return -1
    else:
        return max(first_case, second_case+1)


print(answer())
