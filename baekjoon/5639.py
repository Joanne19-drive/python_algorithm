import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

num_list = []

while True:
    try:
        num_list.append(int(input()))
    except:
        break

# 풀이 1 : num_list를 계속 넘기는 방식. 메모리 차지를 너무 많이 함.


def ordering(postorder):
    if len(postorder) == 0:
        return
    mid = postorder[0]
    left, right = [], []
    for i in range(1, len(postorder)):
        if postorder[i] > mid:
            left = postorder[1:i]
            right = postorder[i:]
            break
    else:
        left = postorder[1:]

    ordering(left)
    ordering(right)
    print(mid)


ordering(num_list)

# 풀이 2 : 풀이 1을 개선하여 num_list를 넘기는 대신, num_list의 인덱스 값을 넘김. 길이도 짧음.


def ordering(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start+1, end+1):
        if num_list[i] > num_list[start]:
            mid = i
            break

    ordering(start+1, mid-1)
    ordering(mid, end)
    print(num_list[start])


ordering(0, len(num_list)-1)
