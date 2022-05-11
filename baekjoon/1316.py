# 내 코드
num = int(input())
n = 0
for i in range(num):
    word = list(input())
    count = []
    for j in range(len(word)):
        if j == 0:
            count.append(word[j])
        else:
            if word[j-1] != word[j]:
                if word[j] not in count:
                    count.append(word[j])
                else:
                    n += 1
                    break
            else:
                pass
print(num-n)

# 짧은 코드
num = int(input())
n = num
for i in range(num):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            n -= 1
            break
print(n)
