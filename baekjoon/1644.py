import sys

input = sys.stdin.readline

is_prime = [True] * 4000001
for i in range(2, int(4000000 ** 0.5)):
    if is_prime[i] == True:
        for j in range(2*i, 4000001, i):
            is_prime[j] = False

n = int(input())
prime_list = [i for i in range(2, 4000001) if is_prime[i] == True]
p_len = len(prime_list)
for i in range(1, p_len):
    prime_list[i] += prime_list[i-1]

start = 0
end = 0
cnt = 0

while start < len(prime_list) and end < len(prime_list) and start <= end:
    if start == 0:
        part_sum = prime_list[end]
    else:
        part_sum = prime_list[end] - prime_list[start-1]
    if part_sum == n:
        cnt += 1
    if part_sum > n:
        start += 1
        continue
    end += 1

print(cnt)
