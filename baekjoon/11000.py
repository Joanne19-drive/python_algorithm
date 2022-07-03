import sys
import heapq

input = sys.stdin.readline
n = int(input())
time_slot = [list(map(int, input().split())) for _ in range(n)]

time_slot.sort()

room = []
heapq.heappush(room, time_slot[0][1])

for i in range(1, n):
    # room이 heapq이기 때문에 time_slot[i][0]이 room의 첫번쨰 값보다 작다면
    # 그 다음 값들에 대해서도 time_slot[i]가 병합될 수 없다는 의미이기 때문에 room[0]과만 비교하면 됨.
    if time_slot[i][0] < room[0]:
        heapq.heappush(room, time_slot[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, time_slot[i][1])

print(len(room))
