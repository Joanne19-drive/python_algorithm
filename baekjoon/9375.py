t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for i in range(n):
        cloth, cloth_type = input().split()
        if cloth_type in clothes:
            clothes[cloth_type] += 1
        else:
            clothes[cloth_type] = 1
    cloth_value = list(clothes.values())
    days = 1
    for j in cloth_value:
        days *= j+1
    print(days - 1)
