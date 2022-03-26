import re

expression = input()
expression = re.split('([-|+])', expression)
minus = False
sum = 0
for ex in expression:
    if ex == "-":
        minus = True
    if ex.isdigit():
        if minus == True:
            sum -= int(ex)
        else:
            sum += int(ex)
print(sum)
