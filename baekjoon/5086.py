while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    factor = False
    multiple = False
    if b % a == 0:
        factor = True
    if a % b == 0:
        multiple = True
    if factor == True:
        print("factor")
    elif multiple == True:
        print("multiple")
    else:
        print("neither")
