import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

cnt = 0

while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    cnt += a + b
    heapq.heappush(heap, a + b)

print(cnt)
