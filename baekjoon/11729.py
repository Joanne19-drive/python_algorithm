# 풀이 1
import copy


def stock(n):
    if n == 1:
        time = 1
        move = [[1, 3]]
        return time, move
    time, move = stock(n-1)
    time = time*2 + 1
    new_move = copy.deepcopy(move)
    for m in new_move:
        for i in range(2):
            if m[i] == 2:
                m[i] = 3
            elif m[i] == 3:
                m[i] = 2
    new_move.append([1, 3])
    for k in move:
        for j in range(2):
            if k[j] == 1:
                k[j] = 2
            elif k[j] == 2:
                k[j] = 1
    new_move += move
    return time, new_move


n = int(input())
time, move = stock(n)
print(time)
for m in move:
    print(*m)


# 풀이 2
def move(n, s, e):
    if n == 1:
        print(s, e)
        return
    move(n-1, s, 6-s-e)
    print(s, e)
    move(n-1, 6-s-e, e)


n = int(input())
time = 1
for i in range(1, n):
    time = time * 2 + 1
print(time)
move(n, 1, 3)
