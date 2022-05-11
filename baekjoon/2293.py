import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

arr = [0] * (k + 1)
arr[0] = 1

for c in coin:
    for i in range(c, k+1):
        # 이미 i 크기의 수를 만들 수 있는 경우의 수에
        # i에서 c를 뺀 수를 만들 수 있는 경우의 수(즉 c만 추가되면 i를 만들 수 있는 경우의 수)를 더하기
        arr[i] += arr[i-c]

print(arr[-1])
