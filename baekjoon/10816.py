from collections import Counter
import sys

# 풀이 1: 이분탐색
n = int(sys.stdin.readline())
scard = list(map(int, sys.stdin.readline().split()))
scard.sort()
m = int(sys.stdin.readline())
fcard = list(map(int, sys.stdin.readline().split()))

# 리스트 자체만 놓고 찾으려고 하면 시간초과가 떠서 딕셔너리 사용
count = {}
for card in scard:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

scard = sorted(list(set(scard)))
n = len(scard)


def binarySearch(a):
    start = 0
    end = n - 1
    mid = (n-1)//2

    while end - start >= 0:
        if a < scard[mid]:
            end = mid - 1
        elif a > scard[mid]:
            start = mid + 1
        else:
            return count[a]
        mid = (end + start)//2
    return 0


for i in range(m):
    print(binarySearch(fcard[i]), end=" ")

# 풀이 2: Counter 사용
n = int(sys.stdin.readline())
scard = list(map(int, sys.stdin.readline().split()))
scard.sort()
m = int(sys.stdin.readline())
fcard = list(map(int, sys.stdin.readline().split()))

c = dict(Counter(scard))
for k in fcard:
    print(c[k] if k in c else 0, end=" ")
