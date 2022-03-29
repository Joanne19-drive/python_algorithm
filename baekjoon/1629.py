import sys
a, b, c = map(int, sys.stdin.readline().split())

# 나머지 분배 법칙 : (A X B) % C = (A % C)*(B % C) % C


def expo(a, n):
    if n == 1:
        return a % c
    else:
        m = expo(a, n//2)
        if n % 2 == 1:
            return (m * m * (a % c)) % c
        else:
            return (m * m) % c


print(expo(a, b))
