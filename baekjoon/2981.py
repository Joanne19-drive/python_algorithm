import math

t = int(input())
num = []

for i in range(t):
    num.append(int(input()))

num2 = []
for j in range(t):
    if j == t-1:
        num2.append(abs(num[j]-num[0]))
    else:
        num2.append(abs(num[j]-num[j+1]))

gcd = num2[0]
for k in range(1, t-1):
    gcd = math.gcd(gcd, num2[k])

m = []

for i in range(1, int(gcd**(1/2)) + 1):
    if (gcd % i == 0):
        m.append(i)
        if ((i**2) != gcd):
            m.append(gcd // i)

m.sort()
m.pop(0)

print(*m)
