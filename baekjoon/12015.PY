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


a = [0]
for i in arr:
    if i > a[-1]:
        a.append(i)
    elif i < a[-1]:
        ind = findIndex(i)
        a[ind] = i

print(len(a)-1)
