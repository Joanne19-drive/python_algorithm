# 풀이 1
# 문자열을 잘라서 그대로 비교하는 방식. 효율 최고.

S = input()
explode_S = input()
explode_length = len(explode_S)

last_char = explode_S[-1]
stack = []

for char in S:
    stack.append(char)
    if stack[-1] == last_char and ''.join(stack[-explode_length:]) == explode_S:
        del stack[-explode_length:]

print(''.join(stack) if stack != [] else "FRULA")

# 풀이 2
# for문 돌려가면서 문자열 비교하는 방식. 코드도 길고 시간도 2배 걸림.

S = input()
explode_S = input()
explode_length = len(explode_S)

last_char = explode_S[-1]
stack = []

for char in S:
    stack.append(char)
    if stack[-1] == last_char and len(stack) >= explode_length:
        flag = True
        for i in range(explode_length):
            if explode_S[-1-i] != stack[-1-i]:
                flag = False
                break
        if flag:
            for i in range(explode_length):
                stack.pop()

print(''.join(stack) if stack != [] else "FRULA")
