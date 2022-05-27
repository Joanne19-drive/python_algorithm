import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
line = [[] for _ in range(n+1)]
costs = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    line[start].append([end, cost])
a, b = map(int, input().split())

res = [1e9]*(n+1)
res[a] = 0
path = [0] * (n+1)
q = []
heapq.heappush(q, [0, a])

# 다익스트라를 활용해서 최소 비용 구하기. 안그러면 계속 시간초과 뜸.
while q:
    current_cost, city = heapq.heappop(q)
    if city == b:
        break
    for next_city, c in line[city]:
        if res[next_city] > current_cost + c:
            res[next_city] = current_cost + c
            path[next_city] = city
            heapq.heappush(q, [current_cost + c, next_city])

p = b
ans = []
while p != 0:
    ans.append(p)
    p = path[p]

print(res[b])
print(len(ans))
print(*ans[::-1])
