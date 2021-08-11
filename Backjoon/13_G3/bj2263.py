# 2263. 트리의 순회

def preOrder(in_start, in_end, po_start, po_end):
    if in_start > in_end or po_start > po_end:
        return

    parents = postorder[po_end]
    print(parents, end=' ')

    left = position[parents] - in_start # 왼쪽 인자의 갯수(inorder에서 parents의 왼쪽 갯수를 postorder에서 빼줘야 다음 루트를 찾기 때문)
    right = in_end - position[parents] # 오른쪽 인자의 갯수

    preOrder(in_start, in_start+left-1, po_start, po_start+left-1) # in_start+left와 po_start+left가 루트를 가르기므로 -1해줘야 함
    preOrder(in_end-right+1, in_end, po_end-right, po_end-1) # 그냥 po_end하면 루트에서 계속 반복하므로 -1

import sys

sys.setrecursionlimit(10**6)
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0] * (N+1)
for i in range(N): # 인덱스: 노드 번호 // 인덱스값: 순서(앞에서부터 0 ~ N-1)
    position[inorder[i]] = i

preOrder(0, N-1, 0, N-1) # inorder 시작, inorder 끝, postorder 시작, postorder 끝

'''
15
8 4 9 2 10 5 11 1 12 6 13 3 14 7 15
8 9 4 10 11 5 2 12 13 6 14 15 7 3 1
'''