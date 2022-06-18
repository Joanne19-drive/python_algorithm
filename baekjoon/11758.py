dots = [list(map(int, input().split())) for _ in range(3)]

# 벡터 외적


def circle(dots):
    x1, y1 = dots[0]
    x2, y2 = dots[1]
    x3, y3 = dots[2]

    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)


res = circle(dots)
if res > 0:
    print(1)
elif res < 0:
    print(-1)
else:
    print(0)
