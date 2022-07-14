import sys

input = sys.stdin.readline

S = input()
text = {S[j:j+i] for i in range(1, len(S)+1) for j in range(len(S) - i)}
print(len(text))
