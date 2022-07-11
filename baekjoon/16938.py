from itertools import combinations
import sys

input = sys.stdin.readline

# 풀이 1: 재귀
n, l, r, x = map(int, input().split())
questions = sorted(list(map(int, input().split())))

ans = 0


def select_question(turn, start, end, level_sum):
    global ans

    if turn == n:
        return

    select_question(turn+1, start, end, level_sum)
    if start == 0 and end == 0:
        if l <= questions[turn] <= r and x == 0:
            ans += 1
        select_question(turn+1, questions[turn],
                        questions[turn], questions[turn])
    elif start != 0:
        if (l <= level_sum+questions[turn] <= r) and (questions[turn] - start >= x):
            ans += 1
        select_question(
            turn+1, start, questions[turn], level_sum+questions[turn])


select_question(0, 0, 0, 0)
print(ans)

# 풀이 2: 조합

n, l, r, x = map(int, input().split())
questions = sorted(list(map(int, input().split())))
select = [comb for i in range(n+1) for comb in combinations(
    questions, i) if l <= sum(comb) <= r and comb[-1]-comb[0] >= x]

print(len(select))
