import sys

# 풀이 1
n, b = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def multiplying(A, B):
    sum_list = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                sum_list[i][j] += A[i][k]*B[k][j]
            sum_list[i][j] %= 1000
    return sum_list


def expoMatrix(b):
    if b == 1:
        for x in range(n):
            for y in range(n):
                matrix[x][y] %= 1000
        return matrix
    else:
        m = expoMatrix(b//2)
        if b % 2 == 0:
            return multiplying(m, m)
        else:
            return multiplying(multiplying(m, m), matrix)


result = expoMatrix(b)
for re in result:
    print(*re)


# 풀이 2

n, b = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def expoMatrix(b):
    if b == 1:
        for x in range(n):
            for y in range(n):
                matrix[x][y] %= 1000
        return matrix
    else:
        m = expoMatrix(b//2)
        sum_list = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for p in range(n):
                    sum_list[i][j] += m[i][p]*m[p][j]
                sum_list[i][j] %= 1000
        if b % 2 == 0:
            return sum_list
        else:
            odd_sum = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for p in range(n):
                        odd_sum[i][j] += sum_list[i][p]*matrix[p][j]
                    odd_sum[i][j] %= 1000
            return odd_sum


result = expoMatrix(b)
for re in result:
    print(*re)
