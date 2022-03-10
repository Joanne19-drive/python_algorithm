a, b, c = map(int, sorted(input().split()))
if a != b and b != c and c != a:
    print(c*100)
elif a == b == c:
    print(10000+a*1000)
else:
    if a == b or a == c:
        k = a
    else:
        k = b
    print(1000+k*100)
