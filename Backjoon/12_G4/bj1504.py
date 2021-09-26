# 1504. 특정한 최단 경로

# 방법1. 다익스트라

def dijkstra(start):
    DP = [INF] * (N+1)  # 다른 노드와의 거리
    DP[start] = 0  # 시작 노드만 0으로 초기화
    bfs_list = []
    heappush(bfs_list, [0, start])  # 비용이 적은 순으로 나오게 heap 생성

    while bfs_list:
        node_dist, node = heappop(bfs_list)

        if DP[node] < node_dist:  # 이동 시간이 기존보다 큰 경우(볼 필요가 없음)
            continue

        for next_node, dist in node_map[node]:
            next_dist = node_dist + dist
            if DP[next_node] > next_dist:  # 이동 시간이 더 적은 경우
                DP[next_node] = next_dist
                heappush(bfs_list, [next_dist, next_node])
    return DP


import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N, M = map(int, input().split())
node_map = [[] for _ in range(N+1)]
INF = 10**7  # 800*1000*2 이상이 되어야 하는 것 같음

for i in range(M):  # 양방향 그래프 채워주기
    a, b, c = map(int, input().split())
    node_map[a].append((b, c))
    node_map[b].append((a, c))

v1, v2 = map(int, input().split())

result_1 = dijkstra(1)
result_v1 = dijkstra(v1)
result_v2 = dijkstra(v2)

result = min([result_1[v1]+result_v1[v2]+result_v2[N], result_1[v2]+result_v2[v1]+result_v1[N]])  # 단 두가지의 경우만 나옴(이 중 최소를 저장)

print(result if result < INF else -1)

# 방법2. bfs

# def bfs(start, *arrive):
#     DP = [INF] * (N+1)  # 다른 노드와의 거리
#     DP[start] = 0  # 시작 노드만 0으로 초기화
#     bfs_list = []
#     heappush(bfs_list, [0, start])  # 비용이 적은 순으로 나오게 heap 생성

#     while bfs_list:
#         node_dist, node = heappop(bfs_list)

#         if DP[node] < node_dist:  # 이동 시간이 기존보다 큰 경우(볼 필요가 없음)
#             continue

#         for next_node, dist in node_map[node].items():  # 딕셔너리이므로 아이템으로 받음
#             next_dist = node_dist + dist
#             if DP[next_node] > next_dist:  # 이동 시간이 더 적은 경우
#                 DP[next_node] = next_dist
#                 heappush(bfs_list, [next_dist, next_node])
#     return [DP[i] for i in arrive]


# import sys
# from heapq import heappush, heappop

# input = sys.stdin.readline
# N, M = map(int, input().split())
# node_map = [{} for _ in range(N+1)]  # 딕셔너리가 더 불러오는 속도가 빠름
# INF = 10**7  # 800*1000*2 이상이 되어야 하는 것 같음

# for i in range(M):  # 양방향 그래프 채워주기
#     a, b, c = map(int, input().split())
#     if b in node_map[a]:
#         node_map[a][b] = min(node_map[a][b], c)
#         node_map[b][a] = min(node_map[b][a], c)
#     else:
#         node_map[a][b] = c
#         node_map[b][a] = c

# v1, v2 = map(int, input().split())

# v1_1, v1_v2, v1_N = bfs(v1, 1, v2, N)  # v1부터 한 이뉴는 양방향 그래프이기 때문에 v_1->1, v_1->v_2, v_1->N을 한 번에 구한 것(1->v1이랑 v1->1이 같은데 다른 간선도 마찬가지)
# v2_1, v2_N = bfs(v2, 1, N)  # 같은 이유로 v_2->1, v_2->N을 구함

# result = min(v1_1+v2_N, v2_1+v1_N) + v1_v2  # (v1->1 + v2->N)과 (v2->1 + v1->N) 중에서 무엇이 더 빠른지 비교하는 것 (v1->v2는 무조건 포함되므로 그냥 더함)
# print(result if result < INF else -1)
