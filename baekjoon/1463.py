n = int(input())

a = [0] * (n+1)

for i in range(2, n+1):
    a[i] = a[i-1] + 1
    # elif 말고 if로 해줘야 함. 6의 배수는 i%3, i%2 둘 다 지나가야 하기 떄문에
    if i % 3 == 0:
        a[i] = min(a[i], a[i//3]+1)

    if i % 2 == 0:
        a[i] = min(a[i], a[i//2]+1)

print(a[n])
