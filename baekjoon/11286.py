import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    a = int(input())
    if a:
        heapq.heappush(heap, (abs(a), a))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
