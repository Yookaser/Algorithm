# 11403. 경로 찾기

# 방법1. bfs
def bfs(n):
    state = [] # n번째에서 방문한 요소들을 저장할 공간
    visited_list = deque([n])

    while visited_list:
        value = visited_list.popleft()
        for next in range(N):
            if node_map[value][next] == 1 and next not in state: # node가 연결되어 있고, 방문한 적 없는 경우
                state.append(next) # 방문한 것으로 변경
                visited_list.append(next)

    return state
    
import sys
from collections import deque

N = int(input())
node_map = [[] for _ in range(N)]

for i in range(N):
    node_map[i] = list(map(int, input().split()))

for i in range(N):
    connect = bfs(i) # return 값(i번째 노드에서 방문한 요소) connect에 저장
    for j in range(N):
        if j in connect: # j가 connect에 있는 경우
            print(1, end=' ') # 1 print
        else:
            print(0, end=' ') # 0 print
    print()

# 방법2. dfs
# def dfs(n):
#     for i in range(N):
#         if node_map[n][i] == 1 and visited_list[i] == 0: # 노드가 연결되어 있고, 방문한 적 없는 경우
#             visited_list[i] = 1 # 방문한 것으로 변경
#             dfs(i) # 재귀

# N = int(input())
# node_map = [[] for _ in range(N)]

# for i in range(N):
#     node_map[i] = list(map(int, input().split()))

# for i in range(N):
#     visited_list = [0] * N # 방문했는지 여부를 체크할 리스트(0: 방문 안함, 1: 방문함)
#     dfs(i) # dfs를 수행하면 위의 visited_list 요소값이 변경됨
#     for j in range(N):
#         if visited_list[j]: # visited_list가 1인 경우
#             print(1, end=' ')
#         else: #  visited_list가 0인 경우
#             print(0, end=' ')
#     print()