import sys

input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a, b, c, d = [x1, y1], [x2, y2], [x3, y3], [x4, y4]


def ccw(a, b, c):
    C = (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - \
        (b[0]*a[1] + c[0]*b[1] + a[0]*c[1])
    if C > 0:
        return 1
    elif C < 0:
        return -1
    else:
        return 0


# 세 점이 일직선 위에 있는 경우는 없다고 했기 때문에 cww() == 0 일 때의 조건은 고려하지 않아도 됨.
print(1 if ccw(a, b, c)*ccw(a, b, d) <
      0 and ccw(c, d, a)*ccw(c, d, b) < 0 else 0)
