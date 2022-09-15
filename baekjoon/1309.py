import sys

input = sys.stdin.readline

N = int(input())

cage = [1, 1, 1]

for i in range(1, N):
    new_cage = [(cage[1] + cage[2]) % 9901, (cage[0] + cage[2]) %
                9901, (cage[0] + cage[1] + cage[2]) % 9901]
    cage = new_cage[:]

print(sum(cage) % 9901)
