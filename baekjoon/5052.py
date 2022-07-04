import sys

input = sys.stdin.readline

# 풀이1 : trie 활용
t = int(input())


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            current_node = current_node.children[char]

        if current_node.children:
            return False
        else:
            return True


for _ in range(t):
    n = int(input())
    numbers = [input().rstrip() for i in range(n)]
    trie = Trie()
    for num in numbers:
        trie.insert(num)

    flag = True
    for num in numbers:
        if not trie.search(num):
            flag = False

    print("YES" if flag else "NO")


# 풀이 2 : 간단함.
t = int(input())

for _ in range(t):
    n = int(input())
    numbers = [input().rstrip() for i in range(n)]
    numbers.sort()
    flag = True
    for i in range(n-1):
        prefix = numbers[i]
        if prefix == numbers[i+1][:len(prefix)]:
            flag = False
            break
    print("YES" if flag else "NO")
