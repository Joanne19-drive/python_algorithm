import sys
from itertools import combinations  # 하나의 리스트에서 모든 조합 구하기

input = sys.stdin.readline

# 문제의 핵심 : 주어진 집합(물건의 무게)의 부분집합의 합이 가방의 크기(최대 넣을 수 있는 무게)보다 작은 것의 개수 구하기
n, c = map(int, input().split())
weights = list(map(int, input().split()))

left = weights[:n//2]
right = weights[n//2:]

left_subset = []
right_subset = []

# 전체 집합을 절반씩 나누어서 각 부분집합에서 나올 수 있는 합을 찾음
for i in range(len(left) + 1):
    for subset in combinations(left, i):
        left_subset.append(sum(subset))

for i in range(len(right) + 1):
    for subset in combinations(right, i):
        right_subset.append(sum(subset))

# left를 기준으로 right의 각각의 값과 합쳐질 수 있는 무게를 이분탐색으로 찾기 위해 left를 정렬
left_subset.sort()

ans = 0

for right_value in right_subset:
    if right_value > c:
        continue

    start = 0
    end = len(left_subset)
    while start < end:
        mid = (start + end) // 2
        if right_value + left_subset[mid] > c:
            end = mid
        else:
            start = mid + 1

    ans += end

print(ans)
