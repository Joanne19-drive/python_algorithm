import sys

input = sys.stdin.readline

n, k = map(int, input().split())
total_plus = 0

# n을 2진법으로 바꾼 수에 들어있는 1의 개수가 주어진 n개의 물병을 합쳐서 만들 수 있는 최소 물병 개수
# 2진법으로 나타낸 n 안에 있는 1의 개수를 줄여서 k 이하로 만드는 것이 핵심
while bin(n).count('1') > k:
    for i in range(len(bin(n))-1, 1, -1):
        if bin(n)[i] == '1':
            total_plus += 2 ** (len(bin(n)) - 1 - i)
            n += 1 << (len(bin(n)) - 1 - i)
            break

print(total_plus)
