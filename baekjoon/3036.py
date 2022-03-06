import math
t = int(input())
rings = list(map(int, input().split()))
for i in range(1, t):
    gcd = math.gcd(rings[0], rings[i])
    print(str(rings[0]//gcd)+"/"+str(rings[i]//gcd))
