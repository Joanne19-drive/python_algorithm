import sys

input = sys.stdin.readline

# 참고 사이트 : https://ko.wikihow.com/다각형-넓이-구하기

n = int(input())
spots = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    next = i + 1 if i != n-1 else 0
    ans += (spots[i][0] * spots[next][1] - spots[i][1] * spots[next][0])

ans /= 2

print(f'{abs(ans):.1f}')
