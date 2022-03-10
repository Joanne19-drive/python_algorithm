n = int(input())
num = list(map(int, input().split()))
operators = list(map(int, input().split()))
result = []


def operating(s, i, a):
    if a == 0:
        return s + num[i]
    elif a == 1:
        return s - num[i]
    elif a == 2:
        return s * num[i]
    else:
        if s < 0:
            return (abs(s)//num[i])*-1
        else:
            return s//num[i]


def dfs(i, sum, op):
    if i == 0:
        sum = num[0]
        dfs(i+1, sum, op)
    else:
        for j in range(4):
            if op[j] > 0:
                if i == n-1:
                    result.append(operating(sum, i, j))
                else:
                    new_op = op[:]
                    new_op[j] -= 1
                    dfs(i+1, operating(sum, i, j), new_op)


dfs(0, 0, operators)

result.sort()
print(result[-1])
print(result[0])
