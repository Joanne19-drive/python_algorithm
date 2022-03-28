n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
minus, zero, one = 0, 0, 0

# 시간은 더 걸리지만 간결한 버전


def nine(x, y, n):
    global minus, zero, one

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != paper[x][y]:
                for l in range(3):
                    for k in range(3):
                        nine(x+l*n//3, y+k*n//3, n//3)
                return
    if paper[x][y] == -1:
        minus += 1
        return
    elif paper[x][y] == 0:
        zero += 1
        return
    else:
        one += 1
        return

# 시간은 더 짧지만 풀어쓴 버전


def nine(x, y, n):
    global minus, zero, one

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != paper[x][y]:
                nine(x, y, n//3)
                nine(x, y+n//3, n//3)
                nine(x, y+n//3*2, n//3)
                nine(x+n//3, y, n//3)
                nine(x+n//3, y+n//3, n//3)
                nine(x+n//3, y+n//3*2, n//3)
                nine(x+n//3*2, y, n//3)
                nine(x+n//3*2, y+n//3, n//3)
                nine(x+n//3*2, y+n//3*2, n//3)
                return
    if paper[x][y] == -1:
        minus += 1
        return
    elif paper[x][y] == 0:
        zero += 1
        return
    else:
        one += 1


nine(0, 0, n)
print(minus)
print(zero)
print(one)
