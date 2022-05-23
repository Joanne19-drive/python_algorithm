import sys

# 풀이1 : 시간도 상대적으로 적게 걸리고, 메모리도 적게 씀. 마지막에 역추적하기 귀찮음.
input = sys.stdin.readline
word1 = input().rstrip()
word2 = input().rstrip()

len1, len2 = len(word1), len(word2)
dp = [[0]*(len2+1) for _ in range(len1+1)]
path = [[(-1, -1) for i in range(len2+1)] for _ in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            path[i][j] = (i-1, j-1)
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                path[i][j] = path[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
                path[i][j] = path[i][j-1]

print(dp[len1][len2])

x, y = path[len1][len2]
ans_word = ''
while x != -1 and y != -1:
    ans_word = word2[y] + ans_word
    x, y = path[x][y]

print(ans_word)


# 풀이2 : 역추적할 필요가 없어서 좋음. 그러나 시간, 메모리 2-3배 팡팡.
input = sys.stdin.readline
word1 = input().rstrip()
word2 = input().rstrip()

len1, len2 = len(word1), len(word2)
res = [['' for i in range(len2+1)] for _ in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if word1[i-1] == word2[j-1]:
            res[i][j] = res[i-1][j-1] + word2[j-1]
        else:
            if len(res[i][j-1]) >= len(res[i-1][j]):
                res[i][j] = res[i][j-1]
            else:
                res[i][j] = res[i-1][j]


print(len(res[len1][len2]))
print(res[len1][len2])
