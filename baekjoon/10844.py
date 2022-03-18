# 풀이 1
n = int(input())
stair1 = [1] * 10
stair1[0] = 0
stair2 = [0] * 10
if n != 1:
    for i in range(1, n):
        if i % 2 == 1:
            for i in range(10):
                if i == 0:
                    stair2[i] = stair1[i+1]
                elif i == 9:
                    stair2[i] = stair1[i-1]
                else:
                    stair2[i] = stair1[i-1] + stair1[i+1]
        else:
            for i in range(10):
                if i == 0:
                    stair1[i] = stair2[i+1]
                elif i == 9:
                    stair1[i] = stair2[i-1]
                else:
                    stair1[i] = stair2[i-1] + stair2[i+1]
if n % 2 == 0:
    print(sum(stair2) % 1000000000)
else:
    print(sum(stair1) % 1000000000)

# 풀이 2
n = int(input())
stair = [[0] * 10 for i in range(n)]

for i in range(n):
    if i == 0:
        for j in range(1, 10):
            stair[i][j] = 1
    else:
        for j in range(10):
            if j == 0:
                stair[i][j] = stair[i-1][j+1]
            elif j == 9:
                stair[i][j] = stair[i-1][j-1]
            else:
                stair[i][j] = stair[i-1][j-1] + stair[i-1][j+1]
print(sum(stair[n-1]) % 1000000000)
