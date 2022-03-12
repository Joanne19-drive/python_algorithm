def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    key = f"{a} {b} {c}"
    if key in cache:
        return cache[key]
    else:
        if a <= b or a <= c:
            answer = 2**a
        else:
            answer = w(a-1, b, c) + w(a-1, b-1, c) + \
                w(a-1, b, c-1) - w(a-1, b-1, c-1)
        cache[key] = answer
        return answer


cache = {}

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        key = f"{a} {b} {c}"
        result = w(a, b, c)
        print(f"w({a}, {b}, {c}) = {result}")
