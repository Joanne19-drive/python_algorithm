import math
a, b = map(int, input().split())
m, n = a, b

# 유클리드 호제법 사용
while n != 0:
    m, n = n, m % n
print(m)
lcm = a * b // m
print(lcm)

# math 함수 사용

gcd = math.gcd(a, b)
lcm = math.lcm(a, b)
print(gcd)
print(lcm)
