from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))
nums = deque([0]*n)
for i in targets:
    nums[i-1] = i
min_rot = 0
for target in targets:
    ind = nums.index(target)
    if ind <= int(len(nums)/2):
        min_rot += ind
        nums.rotate(-ind)
    else:
        min_rot += (len(nums)-ind)
        nums.rotate(len(nums)-ind)
    nums.popleft()
print(min_rot)
