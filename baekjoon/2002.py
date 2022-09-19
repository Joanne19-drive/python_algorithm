import sys

input = sys.stdin.readline

N = int(input())

in_list = {input().rstrip(): i for i in range(N)}
out_list = [input().rstrip() for _ in range(N)]

ans = 0

for i in range(N-1):
    for j in range(i+1, N):
        if in_list[out_list[i]] > in_list[out_list[j]]:
            ans += 1
            break

print(ans)
