t = int(input())
case = [1, 1, 1]

for _ in range(t):
    n = int(input())
    if n <= len(case):
        print(case[n-1])
    else:
        while len(case) < n:
            case.append(case[-2]+case[-3])
        print(case[-1])
