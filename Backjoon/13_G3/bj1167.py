# 1167. 트리의 지름

# 방법1. dfs
def dfs(start, result):
    for node, dist in line[start]:
        if not result[node]:
            result[node] = result[start] + dist
            dfs(node, result)
    return

import sys

input = sys.stdin.readline
V = int(input())
line = [[] for _ in range(V+1)]

for _ in range(V): # 입력 받기(각 노드가 연결된 것이 모두 출력됨 -> 부모에서 자식 노드만 나오는 것이 아님)
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)-1, 2): # step 2씩 움직이게 만듬
        if i == -1:
            break
        line[arr[0]].append((arr[i], arr[i+1]))

result1 = [0] * (V+1) # 1노드에서 다른 노드까지의 거리를 저장할 리스트
dfs(1, result1) # 아무 노드(여기선 1)에서 다른 노드로 가는 비용 계산
result1[1] = 0 # 연결 노드? 양방향?이라 다른 노드에서 1로 오는 거리도 계산되므로 초기화 함

distant = 0
dist_node = 0
for i in range(len(result1)): # 가장 긴 노드값과 인덱스 찾기
    if result1[i] > distant:
        distant = result1[i]
        dist_node = i

result2 = [0] * (V+1) # 1노드에서 가장 먼 노드(트리의 지름의 한 노드)와 다른 노드까지의 거리를 저장할 리스트
dfs(dist_node, result2) # 1노드에서 가장 먼 노드에서 다른 노드로 가는 비용 계산
result2[dist_node] = 0 # 초기화
print(max(result2)) # 트리의 지름 출력(1에서 가장 먼 노드 ~ 해당 노드에서 가장 먼 노드까지의 거리)

# 방법2. bfs
# def bfs(start):
#     visited = set([start])
#     bfs_list = deque([start])
#     result = [0] * (V+1) # 다른 노드와의 거리를 저장할 리스트

#     while bfs_list:
#         node = bfs_list.popleft()
#         for next_node, dist in line[node]:
#             if next_node not in visited: # 이동할 수 있는 노드가 방문한 적 없는 경우('result[next_node] != 0'로 해도 되지만, 첫 start를 다시 방문하지 않기 위해서)
#                 visited.add(next_node)
#                 bfs_list.append(next_node)
#                 result[next_node] = result[node] + dist # 거리 계산하여 입력함
#     return result

# import sys
# from collections import deque

# input = sys.stdin.readline
# V = int(input())
# line = [[] for _ in range(V+1)]

# for i in range(1, V+1): # 입력 받기
#     arr = tuple(map(int, input().split())) # 튜플로 받은 이유는 리스트보다 빠를 줄 알았으나 백준에서는 리스트가 더 빨랐음...
#     for j in range(1, len(arr), 2): # step 2씩 움직이게 만듬
#         if arr[j] == -1:
#             break
#         line[arr[0]].append((arr[j], arr[j+1]))

# result1 = bfs(1) # 아무 노드(여기선 1)에서 다른 노드로 가는 비용을 반환 받음
# result2 = bfs(result1.index(max(result1))) # 1노드에서 가장 먼 노드(트리의 지름의 한 쪽이 됨)에서 다른 노드로 가는 비용을 반환 받음
# print(max(result2)) # 트리의 지름이 되는 한 노드와 가장 멀리 있는 노드의 거리를 출력