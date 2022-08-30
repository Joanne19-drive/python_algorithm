import sys

input = sys.stdin.readline

N = int(input())
targets = list(map(int, input().split()))

arrow = [0] * 1_000_002  # t가 1_000_000일 때 arrow의 1_000_001 인덱스를 필요로 함

for t in targets:
    if arrow[t+1] >= 1:
        arrow[t+1] -= 1
    arrow[t] += 1

print(sum(arrow))
