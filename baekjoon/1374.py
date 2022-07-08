import sys
import heapq

input = sys.stdin.readline

n = int(input())

subjects = []

for i in range(n):
    subject, start, end = map(int, input().split())
    subjects.append((start, end))

subjects.sort()
timetable = []
heapq.heappush(timetable, subjects[0][1])

for i in range(1, n):
    if subjects[i][0] >= timetable[0]:
        heapq.heappop(timetable)
    heapq.heappush(timetable, subjects[i][1])

print(len(timetable))
