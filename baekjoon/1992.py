n = int(input())
tree = [input() for _ in range(n)]

comp = ''


def quad(x, y, n):
    global comp

    for i in range(x, x+n):
        for j in range(y, y+n):
            if tree[i][j] != tree[x][y]:
                comp += '('
                quad(x, y, n//2)
                quad(x, y+n//2, n//2)
                quad(x+n//2, y, n//2)
                quad(x+n//2, y+n//2, n//2)
                comp += ")"
                return
    if tree[x][y] == '1':
        comp += '1'
        return
    else:
        comp += '0'
        return


quad(0, 0, n)
print(comp)
