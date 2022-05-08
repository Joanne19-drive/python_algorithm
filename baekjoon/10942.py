import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
palindrome = [[-1] * n for _ in range(n)]
for i in range(n):
    palindrome[i][i] = 1

for j in range(1, n):
    for i in range(j-1, -1, -1):
        if palindrome[i+1][j-1] == -1 and arr[j] == arr[j-1]:
            palindrome[i][j] = 1
            continue
        if palindrome[i+1][j-1] == 1 and arr[i] == arr[j]:
            palindrome[i][j] = 1
            continue
        palindrome[i][j] = 0

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(palindrome[s-1][e-1])
