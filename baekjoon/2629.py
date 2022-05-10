import sys

input = sys.stdin.readline

# 풀이 1: dp
n = int(input())
grams = list(map(int, input().split()))
m = int(input())
marble = list(map(int, input().split()))

dp = [[False for i in range(40001)] for _ in range(n+1)]


def dfs(idx, weight):
    if dp[idx][weight]:
        return
    dp[idx][weight] = True

    if idx != n-1:
        dfs(idx+1, weight)
        dfs(idx+1, weight + grams[idx+1])
        dfs(idx+1, abs(weight - grams[idx+1]))


dfs(0, 0)
dfs(0, grams[0])


for i in marble:
    if dp[n-1][i]:
        print('Y', end=' ')
    else:
        print('N', end=' ')

# 풀이 2: set - 훨씬 간결하고 알아먹기 쉽다.........
n = int(input())
gram = list(map(int, input().split()))
m = int(input())
marble = list(map(int, input().split()))

possible = [0, gram[0]]
if n > 1:
    for i in gram[1:]:
        a = []
        for j in possible:
            a.extend([j+i, abs(j-i), j])
        possible.extend(a)
        possible = list(set(possible))


for k in marble:
    print('Y' if k in possible else 'N', end=' ')
