import sys

input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

    def show(self, num):
        if self.key != None:
            print('--'*num + self.key)
        sorted_children = sorted(self.children.keys())
        for child in sorted_children:
            self.children[child].show(num+1)


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, words):
        current_node = self.head

        for word in words:
            if word not in current_node.children:
                current_node.children[word] = Node(word)
            current_node = current_node.children[word]

        current_node.data = words


n = int(input())

trie = Trie()
for _ in range(n):
    robot_data = input().split()
    trie.insert(robot_data[1:])

trie.head.show(-1)
