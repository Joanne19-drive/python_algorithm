import sys

input = sys.stdin.readline
t = int(input())

# 신장 트리를 이용한 문제
for _ in range(t):
    n, m = map(int, input().split())

    for i in range(m):
        a, b = map(int, input().split())

    # n개의 국가를 모두 방문하기 위해서는 n-1번만 비행기를 타는 것이 가장 적게 비행기를 타는 방법
    print(n-1)

'''
신장 트리(spanning tree)
n개의 정점을 가지는 그래프의 최소 간선의 수는 (n-1)개이고, (n-1)개의 간선으로 연결되어 있으면 필연적으로 트리 형태가 되고 이것이 바로 Spanning Tree가 된다.
'''
