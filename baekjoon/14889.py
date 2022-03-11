from itertools import combinations as co
# permuations와 combinations는 각각 순열과 조합을 찾아주는 아이라고 함

n = int(input())
player = [i for i in range(n)]
combo = []
for _ in range(n):
    combo.append(list(map(int, input().split())))

min_gap = 10000
team = list(co(player, n//2))

for i in range(len(team)//2):
    tA = 0
    tB = 0
    for a1 in range(n//2-1):
        for a2 in range(a1, n//2):
            tA += combo[team[i][a1]][team[i][a2]]
            tA += combo[team[i][a2]][team[i][a1]]
    for b1 in range(n//2-1):
        for b2 in range(b1, n//2):
            tB += combo[team[-1-i][b1]][team[-1-i][b2]]
            tB += combo[team[-1-i][b2]][team[-1-i][b1]]
    if min_gap > abs(tA-tB):
        min_gap = abs(tA-tB)

print(min_gap)
