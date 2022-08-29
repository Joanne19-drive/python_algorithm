import sys

input = sys.stdin.readline


def pelindrome(string):
    if string == string[::-1]:
        return 0
    else:
        left, right = 0, len(string) - 1
        while left < right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                check1, check2 = pseudo_pelindrome(
                    string, left+1, right), pseudo_pelindrome(string, left, right-1)
                if check1 or check2:
                    return 1
                else:
                    return 2


def pseudo_pelindrome(string, left, right):
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


n = int(input())

for _ in range(n):
    string = input().rstrip()
    print(pelindrome(string))
