n = int(input())
road_length = list(map(int, input().split()))
ppl = list(map(int, input().split()))
low_price = 0
total_oil = 0
for i in range(n-1):
    if i == 0:
        low_price = ppl[0]
    else:
        low_price = min(low_price, ppl[i])
    total_oil += low_price * road_length[i]
print(total_oil)
