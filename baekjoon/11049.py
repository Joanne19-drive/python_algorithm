import sys

input = sys.stdin.readline


def dp(n, matrix):
    result = [[0] * n for _ in range(n)]
    for j in range(1, n):
        for i in range(j-1, -1, -1):
            result[i][j] = min(result[i][k] + result[k+1][j] + matrix[i]
                               [0]*matrix[k][1]*matrix[j][1] for k in range(i, j))
    return result[0][-1]


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(dp(n, matrix))
