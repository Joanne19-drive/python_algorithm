import sys
import math

input = sys.stdin.readline
n, p, q = map(int, input().split())

# 리스트가 아닌 딕셔너리에 저장해야 시간 초과나 메모리 초과가 나지 않는다...
dictionary = {}
dictionary[0] = 1


def dp(i):
    if i in dictionary:
        return dictionary[i]
    dictionary[i] = dp(math.floor(i/p)) + dp(math.floor(i/q))
    return dictionary[i]


print(dp(n))
