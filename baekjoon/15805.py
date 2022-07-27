import sys

input = sys.stdin.readline

n = int(input())
route = list(map(int, input().split()))
city_cnt = max(route) + 1
parent = [-1] * city_cnt
visited = [False] * city_cnt
visited[route[0]] = True

for i in range(1, n):
    if not visited[route[i]]:
        parent[route[i]] = route[i-1]
        visited[route[i]] = True

print(city_cnt)
print(*parent)
