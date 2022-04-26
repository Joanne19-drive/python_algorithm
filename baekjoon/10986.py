import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
# 숫자 자체를 하나씩 비교해서 빼면 시간초과가 나오기 때문에
# 같은 나머지 값을 가지는 수의 갯수를 찾아서 조합을 사용하면 됨
rest = [0] * m
for i in range(n):
    if i != 0:
        arr[i] += arr[i-1]
    rest[arr[i] % m] += 1
ans = rest[0]
for j in range(m):
    if rest[j] != 0:
        ans += rest[j] * (rest[j]-1) // 2

print(ans)
