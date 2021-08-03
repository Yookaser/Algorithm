# 11724. 연결 요소의 개수

# 방법1. dfs
def dfs(node):
    for i in range(N):
        if node_map[node][i] == 1 and not confirm[i]: # 간선이 있고, 방문한 적 없는 경우
            confirm[i] = True # 방문한 것으로 바꿈
            dfs(i) # 해당 i dfs 실행

import sys

sys.setrecursionlimit(2000) # dfs는 재귀 함수로 최대 재귀 늘려줘야 함(아니면 recursion error)
input = sys.stdin.readline
N, M = map(int, input().split())
cnt = 0 # 카운팅을 할 변수
confirm = [False] * N # 방문했는지 확인할 리스트
node_map = [[0] * N for _ in range(N)] # node와 간선을 나타낼 맵

for _ in range(M):
    u, v = map(int, input().split())
    node_map[u-1][v-1] = node_map[v-1][u-1] = 1 # 방향이 없으므로 무조건 양쪽 다 해줘야 됨 **기억**

for i in range(N): # 모든 노드 반복
    if not confirm[i]: # 방문한 적 없는 경우
        dfs(i) # 해당 i를 dfs 실행
        cnt += 1 # 카운팅 +1

print(cnt)

# 방법2. bfs
# def bfs(node):
#     visited_list = deque([node])

#     while visited_list: # visited_list가 비어있을 때까지
#         value = visited_list.popleft() # 가장 왼쪽 값(노드) 저장
#         for i in range(N):
#             if node_map[value][i] == 1 and not confirm[i]: # 간선이 있고, 방문한 적 없는 경우
#                 confirm[i] = True # 방문한 것으로 바꿈
#                 visited_list.append(i)

# import sys
# from collections import deque

# input = sys.stdin.readline
# N, M = map(int, input().split())
# cnt = 0 # 카운팅을 할 변수
# confirm = [False] * N # 방문했는지 확인할 리스트
# node_map = [[0] * N for _ in range(N)] # node와 간선을 나타낼 맵

# for _ in range(M):
#     u, v = map(int, input().split())
#     node_map[u-1][v-1] = node_map[v-1][u-1] = 1 # 방향이 없으므로 무조건 양쪽 다 해줘야 됨 **기억**

# for i in range(N): # 모든 노드 반복
#     if not confirm[i]: # 방문한 적 없는 경우
#         bfs(i) # 해당 i를 dfs 실행
#         cnt += 1 # 카운팅 +1

# print(cnt)