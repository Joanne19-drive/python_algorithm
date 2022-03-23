n = int(input())
tile = [0] * (n+1)
for i in range(n+1):
    if i < 3:
        tile[i] = i
    else:
        tile[i] = (tile[i-1] + tile[i-2]) % 15746
print(tile[n])
