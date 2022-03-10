hour, minute = map(int, input().split())
minute += int(input())
while minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24
print(hour, minute)
