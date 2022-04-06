n = int(input())
arr = list(map(int, input().split()))


def findIndex(i):
    start = 0
    end = len(a) - 1
    while end >= start:
        mid = (start + end) // 2
        if i < a[mid]:
            end = mid - 1
        elif i > a[mid]:
            start = mid + 1
        else:
            return mid
    return start


a = [0]  # 최장 수열을 저장할 array
for i in arr:
    if i > a[-1]:
        a.append(i)  # 쌓여가는 최장수열의 마지막 값보다 클 경우, a에 추가
    elif i < a[-1]:
        ind = findIndex(i)  # 작을 경우, 얘가 대체할 수 있는 a의 자리를 찾아서
        # (같은 값이나 i보다 작은 수 중 가장 차이가 적은 수의 자리)
        a[ind] = i  # 해당 인덱스에 i값을 집어넣는다.
# 실제 최장 수열을 찾을 필요가 없이 최장 수열의 길이만 출력하면 되기 때문에.
print(len(a)-1)
