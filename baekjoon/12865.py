n, k = map(int, input().split())
weight = [0]
value = [0]
for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)
max_val = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if weight[i] > j:
            max_val[i][j] = max_val[i-1][j]
        else:
            max_val[i][j] = max(max_val[i-1][j], max_val[i-1]
                                [j-weight[i]]+value[i], value[i])
print(max_val[n][k])
