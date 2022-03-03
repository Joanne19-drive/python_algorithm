size = int(input())
divisors = map(int, input().split())
divisors.sort()
if size == 1:
    print(divisors[0]**2)
else:
    print(divisors[0]*divisors[-1])
