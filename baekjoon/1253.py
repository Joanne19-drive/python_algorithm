import sys

input = sys.stdin.readline

# 풀이 1
N = int(input())
array = sorted(list(map(int, input().split())))

cnt = 0

for i in range(N):
    start = 0 if i != 0 else 1
    end = N-1 if i != N-1 else N-2
    target = array[i]
    while start < end:
        if array[start] + array[end] > target:
            end -= 1
        elif array[start] + array[end] < target:
            start += 1
        else:
            cnt += 1
            break
        if start == i:
            start += 1
        if end == i:
            end -= 1

print(cnt)

# 풀이 2
N = int(input())
array = sorted(list(map(int, input().split())))

cnt = 0

for i in range(N):
    temp = array[:i] + array[i+1:]
    start, end = 0, N-2
    target = array[i]
    while start < end:
        if temp[start] + temp[end] > target:
            end -= 1
        elif temp[start] + temp[end] < target:
            start += 1
        else:
            cnt += 1
            break

print(cnt)
