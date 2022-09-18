n = int(input())


def hanoi_tower(step, start, end):
    if step == 1:
        print(start, end)
        return
    middle = 6 - start - end
    hanoi_tower(step-1, start, middle)
    hanoi_tower(1, start, end)
    hanoi_tower(step-1, middle, end)
    return


print(2 ** n - 1)
if n <= 20:
    hanoi_tower(n, 1, 3)
