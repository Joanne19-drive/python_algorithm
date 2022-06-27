import sys
from math import inf as INF
# INF를 여러 방식으로 정의해봤는데 math에서 가져오는 게 시간초과가 안났다. 왜지?,,

input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (1 << n) for _ in range(n)]


def dfs(now, visit):
    if visit == (2 ** n) - 1:
        if cost[now][0]:
            return cost[now][0]
        return INF

    if dp[now][visit]:
        return dp[now][visit]

    left_cost = INF

    for i in range(1, n):
        # 원래는 각각 if (visit & (1 <<i)) > 0: continue, if not cost[now][i]: continue 였는데 하나로 합침
        if not (visit & (1 << i)) and cost[now][i]:
            # 여기서 dp[now][visit] = min(dp[now][visit], dfs(i, visit | (1 << i)) + cost[now][i])를 했는데 시간초과남.
            # dp를 계속 갱신하기보다 다른 변수에 값을 저장했다가 i가 1부터 n-1까지 다 돌고 나서 한 번에 갱신하는 게 더 효율적인 듯.
            temp = dfs(i, visit | (1 << i)) + cost[now][i]
            left_cost = min(left_cost, temp)

    dp[now][visit] = left_cost
    return dp[now][visit]


print(dfs(0, 1))
