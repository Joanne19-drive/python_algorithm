n = int(input())
time = list(map(int, input().split()))
time.sort()
sum = 0
for i in range(n):
    sum += time[i]*(n-i)
print(sum)
