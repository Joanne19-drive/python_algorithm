# 풀이 1

pattern = ['***', '* *', '***']
n = int(input())


def star(n):
    global pattern

    if n == 3:
        return pattern
    pattern *= 3
    l = len(pattern)
    for i in range(l):
        if i < (l//3) or i > (l//3*2-1):
            pattern[i] *= 3
        else:
            pattern[i] = pattern[i] + ' '*len(pattern[i]) + pattern[i]
    star(n//3)


star(n)
for p in pattern:
    print(p)


# 풀이 2
n = int(input())


def star(n):
    if n == 1:
        return ["*"]
    pattern = star(n//3)
    pattern *= 3
    l = len(pattern)
    for i in range(l):
        if i < (l//3) or i > (l//3*2-1):
            pattern[i] *= 3
        else:
            pattern[i] = pattern[i] + ' '*len(pattern[i]) + pattern[i]
    return pattern


pattern = star(n)
for p in pattern:
    print(p)
