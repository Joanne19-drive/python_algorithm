S = input()


def parentheses(S):
    stack = []
    pair = {']': ['[', 3], ')': ['(', 2]}

    cal = []

    for s in S:
        if s in ['[', '(']:
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            now = stack.pop()
            if pair[s][0] == now:
                cal.append([pair[s][1], len(stack)])
            else:
                return 0

    if len(stack) > 0:
        return 0

    result = [cal[0]]
    for i in range(1, len(cal)):
        now = cal[i]

        while len(result) > 0 and result[-1][1] >= now[1]:
            next_cal = result.pop()
            if next_cal[1] > now[1]:
                now[0] *= next_cal[0]
            else:
                now[0] += next_cal[0]

        result.append(now)

    return result[0][0]


print(parentheses(S))
