import sys

sys.setrecursionlimit(10**9)

k = int(input())

# 점화식 참고: https://ko.wikipedia.org/wiki/투에-모스_수열


def ThueMorse(k):
    if k == 0:
        return 0
    elif k % 2 == 0:
        return ThueMorse(k//2)
    else:
        return 1-ThueMorse(k//2)


print(ThueMorse(k-1))
