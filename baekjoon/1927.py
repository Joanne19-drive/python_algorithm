import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    a = int(input())
    if a:
        heapq.heappush(heap, a)

    else:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap))
