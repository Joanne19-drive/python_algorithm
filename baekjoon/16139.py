import sys

input = sys.stdin.readline
s = input()
q = int(input())
# 딕셔너리를 사용하는 만큼 메모리 차지를 너무 많이 한다.
# 딕셔너리 대신 알파벳 길이만큼의 리스트를 사용하는 풀이도 해보면 좋을 듯.
sol = [{}]
for i in range(len(s)):
    new_dict = sol[i].copy()
    if s[i] in sol[i]:
        new_dict[s[i]] += 1
    else:
        new_dict[s[i]] = 1
    sol.append(new_dict)

for _ in range(q):
    letter, start, end = input().split()
    start, end = int(start), int(end)
    if sol[end+1].get(letter):
        if sol[start].get(letter):
            print(sol[end+1][letter]-sol[start][letter])
        else:
            print(sol[end+1][letter])
    else:
        print(0)
