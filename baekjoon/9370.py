import sys
import heapq

input = sys.stdin.readline
INF = 1e9
test = int(input())


def fast_track(start, graph, cross):
    q = []
    track = [INF] * (cross + 1)
    track[start] = 0
    q.append([0, start])

    while q:
        dist, loc = heapq.heappop(q)
        if track[loc] < dist:
            continue
        for node in graph[loc]:
            spot, distance = node
            cost = dist + distance
            if track[spot] > cost:
                track[spot] = cost
                heapq.heappush(q, [cost, spot])

    return track


for _ in range(test):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for k in range(n+1)]
    for k in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
    destination = [int(input()) for k in range(t)]

    min_dist = fast_track(s, graph, n)
    route1 = fast_track(g, graph, n)
    route2 = fast_track(h, graph, n)

    ans = []
    for des in destination:
        real_route1 = [min_dist[g], route1[h], route2[des]]
        real_route2 = [min_dist[h], route2[g], route1[des]]
        if INF in real_route1 and INF in real_route2:
            continue
        possible_route = min(sum(real_route1), sum(real_route2))
        if min_dist[des] == possible_route:
            ans.append(des)

    print(*sorted(ans))
