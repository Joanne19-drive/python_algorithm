import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# root의 위치를 바로 찾기 위해 각 중위순회의 값들의 인덱스를 저장
# 그래서 후위순회의 끝값을 띡 넣으면 그게 중위순회에서 어느 위치에 있는지 알 수 있도록
# 이거 안하고 함수 안에서 for문 돌렸다가 계속 시간초과남..머리를 쓰자^^
position = [0] * (n+1)
for i in range(n):
    position[inorder[i]] = i


def make_preorder(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):  # 둘 중 하나라도 조건이 빠져있으면 무한루프 돌 수 있음
        return
    left_len = 0
    root = postorder[post_end]  # 후위순회의 끝값 == 루트
    left_len = position[root] - in_start  # 루트의 중위순회 인덱스 - 중위순회 시작점 == 왼쪽 노드 길이
    print(root, end=' ')  # 전위순회에서는 루트가 먼저 출력되어야 하니까 먼저 출력하고 빠지기
    make_preorder(in_start, in_start+left_len-1,
                  post_start, post_start+left_len-1)
    make_preorder(in_start+left_len+1, in_end,
                  post_start+left_len, post_end-1)
    return
    # preorder 리스트를 리턴할까 했으나 기껏 메모리 아끼려고 인덱스 썼는데 리턴할 때 리스트 보내면 아낀 의미가 없어져서
    # 걍 위에서 end=' ' 사용해서 루트 나올때마다 바로바로 출력해버림


make_preorder(0, n-1, 0, n-1)
