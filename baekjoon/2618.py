import sys

# 너무 어려워서 구글링한 코드 한줄한줄 따라치며 이해하려고 함.
# https://velog.io/@jini_eun/백준-2618번-경찰차-Java-Python
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
w = int(input())
cases = [(1, 1), (n, n)]+[tuple(map(int, input().split())) for _ in range(w)]

dp = [[-1] * (w+2) for _ in range(w+2)]


def find_way(x, y):
    if x > w or y > w:
        return 0
    if dp[x][y] != -1:
        return dp[x][y]

    nc = max(x, y) + 1  # next_case
    next_x = find_way(
        nc, y) + abs(cases[nc][0] - cases[x][0]) + abs(cases[nc][1] - cases[x][1])
    next_y = find_way(
        x, nc) + abs(cases[nc][0] - cases[y][0]) + abs(cases[nc][1] - cases[y][1])
    dp[x][y] = min(next_x, next_y)

    return dp[x][y]


def back_tracking(x, y):
    if x > w or y > w:
        return

    nc = max(x, y) + 1
    nx = abs(cases[nc][0] - cases[x][0]) + abs(cases[nc][1] - cases[x][1])
    ny = abs(cases[nc][0] - cases[y][0]) + abs(cases[nc][1] - cases[y][1])

    # dp[nc][y] + nx와 dp[x][nc] + ny가 동일하다는 말은 어떤 경찰차가 nc번쨰 사건으로 가든 마지막 사건까지의 거리는 동일하다는 의미이기 때문에
    # 경찰차 1번이 nc번째로 가나 경찰차 2번이 nc번째로 가나 상관 없음.
    # 그래서 if문 조건을 dp[nc][y] + nx <= dp[x][nc] + ny로 해도 되고 dp[nc][y] + nx < dp[x][nc] + ny로 해도 됨.
    if dp[nc][y] + nx <= dp[x][nc] + ny:
        print(1)
        back_tracking(nc, y)
    else:
        print(2)
        back_tracking(x, nc)
    return


print(find_way(0, 1))
back_tracking(0, 1)
