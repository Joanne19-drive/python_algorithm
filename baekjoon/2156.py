import sys

n = int(sys.stdin.readline())
glasses = [0]
for _ in range(n):
    portion = int(sys.stdin.readline())
    glasses.append(portion)

total = [0] * (n+1)
for i in range(1, n+1):
    if i == 1 or i == 2:
        total[i] = glasses[i-1] + glasses[i]
    else:
        total[i] = max(total[i-1], total[i-3]+glasses[i-1] +
                       glasses[i], total[i-2]+glasses[i])

print(total[-1])
