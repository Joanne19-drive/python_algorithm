import sys

input = sys.stdin.readline

n, k = map(int, input().split())
height = list(map(int, input().split()))

# 각 조에서 가장 키가 큰 원생과 가장 키가 작은 원생의 키차이는 앞뒤 원생의 키차이를 조별로 합한 값과 동일.
# 조를 나누는 구간은 가장 키차이가 큰 구간.
c = sorted([height[i] - height[i-1] for i in range(1, n)])

print(sum(c[:n-k]))
