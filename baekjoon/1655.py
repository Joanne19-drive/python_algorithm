import heapq
import sys

input = sys.stdin.readline
n = int(input())
small_h, big_h, mid = [], [], 0

for i in range(n):
    num = int(input())
    if i == 0:
        mid = num
    else:
        if num >= mid:
            heapq.heappush(big_h, num)  # 입력된 값이 중간값보다 크면 big_h에 넣는다
            if len(big_h)-len(small_h) > 1:  # 중간값 뒤에 있는 애들이 많아지면
                heapq.heappush(small_h, (-mid, mid))  # 중간값을 small_h로 보내고
                mid = heapq.heappop(big_h)  # big_h의 첫번쨰값이 중간값이 된다
        else:
            # 입력된 값이 중간값보다 작으면 small_h에 넣는다(나중에 가장 큰 값을 꺼내야 하므로 튜플 형태로 넣는다)
            heapq.heappush(small_h, (-num, num))
            if len(small_h) > len(big_h):  # 중간값 앞에 있는 애들이 많아지면
                heapq.heappush(big_h, mid)  # 중간값을 big_h로 보내고
                mid = heapq.heappop(small_h)[1]  # small_h의 마지막값이 중간값이 된다
    print(mid)
