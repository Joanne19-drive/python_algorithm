import sys

input = sys.stdin.readline
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a, b = (x1, y1), (x2, y2)
c, d = (x3, y3), (x4, y4)

if b < a:
    a, b = b, a
if d < c:
    c, d = d, c


def ccw(a, b, c):
    S = (a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - a[1]*b[0] - b[1]*c[0] - c[1]*a[0])

    if S > 0:
        return 1
    elif S < 0:
        return -1
    else:
        return 0

# 함수 없이 if문을 써봤는데 함수화하는 게 시간이 덜 걸린다.


def ans():
    A1 = ccw(a, b, c) * ccw(a, b, d)
    A2 = ccw(c, d, a) * ccw(c, d, b)

    if A1 == 0 and A2 == 0:
        if a <= d and c <= b:
            return 1
        else:
            return 0
    elif A1 <= 0 and A2 <= 0:
        return 1
    else:
        return 0


print(ans())
