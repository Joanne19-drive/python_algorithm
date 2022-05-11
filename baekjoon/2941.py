alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for a in alphabet:
    word = word.replace(a, 'a')
print(len(word))
