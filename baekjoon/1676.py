a = int(input())
five = 0
for i in range(1, a+1):
    while i % 5 == 0:
        if i % 5 == 0:
            five += 1
            i /= 5
print(five)
