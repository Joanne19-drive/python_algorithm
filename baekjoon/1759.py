import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int, input().split())
characters = sorted(input().split())

all_list = list(combinations(characters, L))


for word in all_list:
    vowel, consonant = 0, 0
    for i in range(L):
        if word[i] in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1
        else:
            consonant += 1
    if vowel >= 1 and consonant >= 2:
        print(''.join(word))
