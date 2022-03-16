n = int(input())
stairs = [0]
for i in range(n):
    score = int(input())
    stairs.append(score)

acc_score = [0]*(n+1)
for i in range(n+1):
    if i == 0:
        continue
    elif i == 1 or i == 2:
        acc_score[i] = stairs[i-1] + stairs[i]
    else:
        acc_score[i] = max(acc_score[i-3]+stairs[i-1],
                           acc_score[i-2]) + stairs[i]
print(acc_score[-1])
