import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)
result = 0

while end >= start:
    mid = (start + end) // 2
    height = sum(i-mid for i in tree if i > mid)  # 이 부분을 풀어서 쓰면 시간초과
    if height >= m:
        start = mid + 1
        result = mid
    elif height < m:
        end = mid - 1


print(result)
