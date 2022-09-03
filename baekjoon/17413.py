S = input() + ' '

start = 0
flag = False
ans = []

for i in range(len(S)):
    if S[i] == '<':
        ans.append(S[start:i][::-1])
        flag = True
        start = i
    elif S[i] == '>':
        ans.append(S[start:i+1])
        start = i+1
        flag = False
    elif S[i] == ' ' and not flag:
        ans.append(S[start:i][::-1])
        ans.append(' ')
        start = i+1

print(''.join(ans))
