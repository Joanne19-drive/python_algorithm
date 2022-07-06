import sys

input = sys.stdin.readline
n, m = map(int, input().split())
books = sorted(list(map(int, input().split())))

minus_position = sorted([book for book in books if book < 0])
plus_position = sorted([book for book in books if book > 0], reverse=True)

total_steps = 0


def walking(direction):
    steps = 0
    i = 0
    while i < len(direction):
        steps += abs(direction[i])
        i += m
    return steps


total_steps += walking(minus_position)
total_steps += walking(plus_position)

print(total_steps * 2 - max(abs(books[0]), abs(books[-1])))
