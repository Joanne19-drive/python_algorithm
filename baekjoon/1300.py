n = int(input())
k = int(input())

start = 1
end = n ** 2

# mid보다 작은 수가 몇개 있는지를 기준으로 일차원 배열일 떄의 인덱스를 확인
while end >= start:
    mid = (start + end) // 2
    count = 0
    for i in range(1, n+1):
        count += min(mid // i, n)
    if count >= k:
        end = mid - 1
    else:
        start = mid + 1

print(start)
