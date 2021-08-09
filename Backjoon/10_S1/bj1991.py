# 1991. 트리 순회

# 방법1. Node class를 이용한 tree
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def preOrder(node): # 전위 순회
    print(tree[node].value, end='')
    if tree[node].left != None:
        preOrder(tree[node].left)
    if tree[node].right != None:
        preOrder(tree[node].right)

def inOrder(node): # 중위 순회
    if tree[node].left != None:
        inOrder(tree[node].left)
    print(tree[node].value, end='')
    if tree[node].right != None:
        inOrder(tree[node].right)

def postOrder(node): # 후위 순회
    if tree[node].left != None:
        postOrder(tree[node].left)
    if tree[node].right != None:
        postOrder(tree[node].right)
    print(tree[node].value, end='')

N = int(input())
tree = {}

for i in range(N):
    node_value = list(map(str, input().split()))
    node_value = [None if i=='.' else i for i in node_value] # '.'값을 None으로 변환(사실 굳이 할 필요는 없음)
    tree[node_value[0]] = Node(node_value[0], node_value[1], node_value[2]) # node_value[0]을 'key'로 'item'은 Node class의 인스턴스로

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')

# 방법2. dict만 이용한 tree
# def preOrder(node): # 전위 순회
#     if node == '.': # 입력값이 없는 경우
#         return
#     print(node, end='')
#     preOrder(tree[node][0])
#     preOrder(tree[node][1])

# def inOrder(node): # 중위 순회
#     if node == '.': # 입력값이 없는 경우
#         return
#     inOrder(tree[node][0])
#     print(node, end='')
#     inOrder(tree[node][1])

# def postOrder(node): # 후위 순회
#     if node == '.': # 입력값이 없는 경우
#         return
#     postOrder(tree[node][0])
#     postOrder(tree[node][1])
#     print(node, end='')

# N = int(input())
# tree = {}

# for i in range(N):
#     node, left, right = map(str, input().split())
#     tree[node] = [left, right] # node를 'key'로 'item'은 좌우값으로

# preOrder('A')
# print()
# inOrder('A')
# print()
# postOrder('A')