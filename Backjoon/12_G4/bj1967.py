# 1967. 트리의 지름

# 방법1. dfs
def dfs(start, result):
    for next_node, dist in tree[start]:
        if not result[next_node]:
            result[next_node] = result[start] + dist
            dfs(next_node, result)

import sys

sys.setrecursionlimit(100000) # 재귀 깊게 해줘야 함
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    parent, child, dist = map(int, input().split())
    tree[parent].append([child, dist])
    tree[child].append([parent, dist]) # 양방향으로 만듬(이거 안하면 두 번째 dfs때 값 제대로 안나오게 됨)

result1 = [0] * (N+1)
dfs(1, result1) # 1이 루트 노드이므로 1부터 시작함
result1[1] = 0 # 양방향이므로 1 -> 1로 가는 값이 0이 아닌 다른 값이 나오게 됨
dist_node = result1.index(max(result1)) # 1에서 가장 멀리 있는 노드

result2 = [0] * (N+1)
dfs(dist_node, result2) # 1에서 가장 멀리 있는 노드와 다른 노드상 거리 찾기
result2[dist_node] = 0 # 위와 마찮가지로 자기자신의 값을 0으로 만들어줘야 함
print(max(result2))

# 방법2. bfs
# def bfs(start):
#     bfs_list = deque([start])
#     result = [0] * (N+1)

#     while bfs_list:
#         node = bfs_list.popleft()
#         for next_node, dist in tree[node]:
#             if not result[next_node]:
#                 bfs_list.append(next_node)
#                 result[next_node] = result[node] + dist
#     return result

# import sys
# from collections import deque

# input = sys.stdin.readline
# N = int(input())
# tree = [[] for _ in range(N+1)]

# for _ in range(N-1):
#     parent, child, dist = map(int, input().split())
#     tree[parent].append([child, dist])
#     tree[child].append([parent, dist]) # 양방향으로 만듬(이거 안하면 두 번째 bfs때 값 제대로 안나오게 됨)

# result1 = bfs(1) # 1이 루트 노드이므로 1부터 시작함
# result1[1] = 0 # 양방향이므로 1 -> 1로 가는 값이 0이 아닌 다른 값이 나오게 됨
# dist_node = result1.index(max(result1))

# result2 = bfs(dist_node) # 1에서 가장 멀리 있는 노드와 다른 노드상 거리 찾고 반환 받기
# result2[dist_node] = 0 # 위와 마찮가지로 자기자신의 값을 0으로 만들어줘야 함
# print(max(result2))