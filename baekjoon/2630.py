n = int(input())
block = [list(map(int, input().split())) for _ in range(n)]
one = 0
zero = 0


def dca(x, y, n):
    global one, zero

    for i in range(x, x+n):
        for j in range(y, y+n):
            if block[i][j] != block[x][y]:
                dca(x, y, n//2)
                dca(x, y+n//2, n//2)
                dca(x+n//2, y, n//2)
                dca(x+n//2, y+n//2, n//2)
                return
    if block[x][y] == 0:
        zero += 1
        return
    else:
        one += 1
        return


dca(0, 0, n)
print(zero)
print(one)
