import sys

n = int(input())
tree = {}
for i in range(n):
    a, b, c = input().split()
    tree[a] = [b, c]

# 풀이 1


def traversal(alpha, way):
    if alpha == '.':
        return ''
    if way == 'pre':
        ans = alpha + traversal(tree[alpha][0], way) + \
            traversal(tree[alpha][1], way)
    elif way == 'in':
        ans = traversal(tree[alpha][0], way) + alpha + \
            traversal(tree[alpha][1], way)
    else:
        ans = traversal(tree[alpha][0], way) + \
            traversal(tree[alpha][1], way) + alpha
    return ans


print(traversal('A', 'pre'))
print(traversal('A', 'in'))
print(traversal('A', 'post'))


# 풀이 2
def preorder_traversal(alpha):
    if alpha == '.':
        return ''
    ans = alpha + \
        preorder_traversal(tree[alpha][0]) + preorder_traversal(tree[alpha][1])
    return ans


def inorder_traversal(alpha):
    if alpha == '.':
        return ''
    ans = inorder_traversal(tree[alpha][0]) + \
        alpha + inorder_traversal(tree[alpha][1])
    return ans


def postorder_traversal(alpha):
    if alpha == '.':
        return ''
    ans = postorder_traversal(tree[alpha][0]) + \
        postorder_traversal(tree[alpha][1]) + alpha
    return ans


print(preorder_traversal('A'))
print(inorder_traversal('A'))
print(postorder_traversal('A'))
