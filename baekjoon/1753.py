import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
distance = [INF] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        dist, point = heapq.heappop(q)

        if distance[point] < dist:
            continue

        for node in graph[point]:
            np, nd = node
            if dist+nd < distance[np]:
                distance[np] = dist+nd
                heapq.heappush(q, [dist+nd, np])


dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
