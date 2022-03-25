n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
count = 0
for coin in reversed(coins):
    count += k//coin
    k %= coin
    if k == 0:
        break
print(count)
