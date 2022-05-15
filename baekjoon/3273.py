import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()  # 투포인터를 정상적으로 사용하기 위해서는 정렬을 반드시 해주어야 한다.
left, right = 0, n-1
ans = 0

while left < right:
    pair = arr[left] + arr[right]

    if pair == x:
        ans += 1
    if pair < x:
        left += 1
        continue
    right -= 1  # right는 pair == x이거나 pair > x일 때 -1이 되어야 하기 때문에 if문 안에 넣지 않음.

print(ans)
