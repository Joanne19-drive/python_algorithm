# python3로 제출했을 때는 시간초과
# pypy3로 제출했더니 통과

n = int(input())
count = 0
queen = [0]*n


def placing(x):
    for i in range(x):
        if queen[i] == queen[x] or abs(queen[i]-queen[x]) == abs(i-x):
            return False

    return True


def n_queen(x):
    global count

    if x == n:
        count += 1

    else:
        for i in range(n):
            queen[x] = i
            if placing(x):
                n_queen(x+1)


n_queen(0)
print(count)
