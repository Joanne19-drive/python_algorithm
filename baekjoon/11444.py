n = int(input())

f = [[1, 1], [1, 0]]


def matrix(a, b):
    new = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                new[i][j] += a[i][k] * b[k][j]
            new[i][j] %= 1000000007
    return new

# 참고 사이트 : https://nukestorm.tistory.com/149


def Fibo(n):
    if n == 1:
        return f
    else:
        two_f = Fibo(n//2)
        if n % 2 == 0:
            return matrix(two_f, two_f)
        else:
            return matrix(matrix(two_f, two_f), f)


if n == 0 or n == 1:
    print(n)
else:
    result = Fibo(n-1)
    print(result[0][0])
