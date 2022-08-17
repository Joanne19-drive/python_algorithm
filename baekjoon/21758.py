import sys

input = sys.stdin.readline

n = int(input())
places = list(map(int, input().split()))
S = [places[0]]
for i in range(1, n):
    S.append(S[-1] + places[i])

honey = 0
# 왼쪽 끝에 꿀이 있을 떄
for i in range(1, n-1):
    honey = max(honey, S[-2] + S[i-1] - places[i])

# 오른쪽 끝에 꿀이 있을 때
for i in range(1, n-1):
    honey = max(honey, S[-1] * 2 - S[0] - S[i] - places[i])

# 가운데에 꿀이 있을 때
for i in range(1, n-1):
    honey = max(honey, S[-2] - places[0] + places[i])

print(honey)
