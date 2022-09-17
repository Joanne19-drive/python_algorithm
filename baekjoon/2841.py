import sys

input = sys.stdin.readline

N, P = map(int, input().split())

guitar = {}

cnt = 0

for _ in range(N):
    line, fret = map(int, input().split())
    if line in guitar:
        while len(guitar[line]) > 0 and guitar[line][-1] > fret:
            guitar[line].pop()
            cnt += 1
        if guitar[line] == [] or (len(guitar[line]) > 0 and guitar[line][-1] < fret):
            guitar[line].append(fret)
            cnt += 1
    else:
        guitar[line] = [fret]
        cnt += 1

print(cnt)
