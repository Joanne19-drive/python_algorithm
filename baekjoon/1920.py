n = int(input())
num = list(map(int, input().split()))
num.sort()
k = int(input())
sample = list(map(int, input().split()))


def binarySearch(a):
    start = 0
    end = n - 1
    mid = (n-1)//2

    while end - start >= 0:
        if a < num[mid]:
            end = mid - 1
        elif a > num[mid]:
            start = mid + 1
        else:
            return 1
        mid = (end + start)//2
    return 0


for i in range(k):
    print(binarySearch(sample[i]))
