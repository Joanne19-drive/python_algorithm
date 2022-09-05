import hashlib

S = input()

print(hashlib.sha256(S.encode()).hexdigest())
