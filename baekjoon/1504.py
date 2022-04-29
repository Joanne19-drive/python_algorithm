import sys
import heapq

input = sys.stdin.readline
INF = 1e9
dot, line = map(int, input().split())
graph = [[] for _ in range(dot + 1)]
for _ in range(line):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, input().split())


def fast_track(start):
    q = []
    track = [INF] * (dot + 1)
    track[start] = 0
    q.append([0, start])

    while q:
        dist, loc = heapq.heappop(q)
        if track[loc] < dist:
            continue
        for node in graph[loc]:
            spot, distance = node
            if track[spot] > dist + distance:
                track[spot] = dist + distance
                heapq.heappush(q, [dist+distance, spot])

    return track


line1 = fast_track(1)
line2 = fast_track(v1)
line3 = fast_track(v2)
final_distance1 = [line1[v1], line2[v2], line3[dot]]
final_distance2 = [line1[v2], line3[v1], line2[dot]]

if INF in final_distance1 and INF in final_distance2:
    print(-1)
else:
    print(min(sum(final_distance1), sum(final_distance2)))
