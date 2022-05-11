word = input()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
n = 0
for letter in word:
    for three in dial:
        for alphabet in three:
            if alphabet == letter:
                n += dial.index(three)+3
print(n)
