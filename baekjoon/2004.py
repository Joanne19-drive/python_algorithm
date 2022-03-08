n, m = map(int, input().split())


def counting(n, k):
    count = 0
    while n:
        n //= k
        # n! 안에 있는 숫자들을 따로 불러와서 계산할 필요 없이 count에 n을 k로 나눈 몫을 더해버림
        # 이를 통해 시간 절약
        count += n
    return count


two = counting(n, 2) - counting(m, 2) - counting(n-m, 2)
five = counting(n, 5) - counting(m, 5) - counting(n-m, 5)

print(min(two, five))
