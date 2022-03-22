str1 = input()
str2 = input()
length1, length2 = len(str1), len(str2)
lcs = [[0]*(length2+1) for _ in range(length1+1)]
for i in range(1, length1+1):
    for j in range(1, length2+1):
        lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
print(lcs[length1][length2])
