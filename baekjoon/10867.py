import sys

input = sys.stdin.readline

n = int(input())
nums = list(set(map(int, input().split())))
print(*sorted(nums))
