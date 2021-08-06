# 5639. 이진 검색 트리

# 방법1. 트리 구현(pypy3)
class Node: # 각 노드는 왼쪽 오른쪽 값을 가짐(트리 구조)
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self): # node를 입력받는게 일반적이나 문제는 없으므로 입력 X
        self.root = None # 대신 None값으로 지정

    def insert(self, value): # 입력 받는 함수
        if self.root == None: # 노드가 없는 경우(노드가 없이 tree가 생성되므로)
            self.root = Node(value) # 노드를 value 지정
        
        else:
            self.current_node = self.root # 루트 다른 변수에 저장
            while True:
                if value < self.current_node.value: # 현재 노드보다 작은 경우
                    if self.current_node.left != None: # 현재 노드 왼쪽 값이 있는 경우
                        self.current_node = self.current_node.left # 왼쪽 값을 현재 노드로
                    else: # 왼쪽값이 없는 경우
                        self.current_node.left = Node(value) # 왼쪽값을 value로 저장
                        break
                else: # 현재 노드보다 큰 경우
                    if self.current_node.right != None: # 현재 노드 오른쪽값이 있는 경우
                        self.current_node = self.current_node.right # 오른쪽 값을 현재 노드로
                    else: # 오른쪽 값이 없는 경우
                        self.current_node.right = Node(value)# 오른쪽 값을 value로 저장
                        break
    
    def postorder(self, node=None): # 후위 순회(루트 노드를 입력 못 받으므로 키워드 인자 사용)
        if node == None:
            node = self.root # root로 저장
        if node.left != None: # 왼쪽 값이 있는 경우
            self.postorder(node.left) # 왼쪽 값으로 재귀
        if node.right != None: # 오른쪽 값이 있는 경우
            self.postorder(node.right) # 오른쪽 값으로 재귀
        print(node.value)

import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
tree = BinaryTree()

while True:
    try:
        tree.insert(int(input()))
    except:
        break

tree.postorder()

# 방법2. 분할 정복
# def postorder(left, right): # left 값보다 큰 값이 나오는 지점을 기준으로 분할해 나가는 함수
#     if left > right: # Base Case
#         return
    
#     div = right + 1 # 분할 지점

#     for i in range(left+1, right+1): # left(맨 왼쪽값)에서 끝까지
#         if num_list[left] < num_list[i]: # 큰 값인 경우
#             div = i # 분할 지점을 저장
#             break

#     postorder(left+1, div-1) # 왼쪽 부분(left보다 작은 구역)
#     postorder(div, right) # 오른쪽 부분(left보다 큰 구역)
#     print(num_list[left])

# import sys

# sys.setrecursionlimit(100000)
# input = sys.stdin.readline
# num_list = []

# while True: # 얼마나 입력받는지 모르므로 try~except 구문 이용
#     try:
#         num_list.append(int(input()))
#     except:
#         break

# postorder(0, len(num_list)-1)