# 1238. 파티

def dijkstra(start, town_map):
    DP = [INF] * (N+1) # 각 노드의 비용은 최대값(10,000*100)으로 초기화(다익스트라)
    DP[start] = 0 # 시작값 0으로
    bfs_list = []
    heappush(bfs_list, [0, start]) # 반드시 비용이 먼저 나와야 함(다익스트라)    

    while bfs_list:
        node_time, node = heappop(bfs_list)

        if DP[node] < node_time: # 이동 시간이 기존보다 큰 경우(볼 필요가 없음)
            continue

        for next_node, time in town_map[node]:
            next_time = node_time + time
            if DP[next_node] > next_time: # 이동 시간이 더 적은 경우
                DP[next_node] = next_time
                heappush(bfs_list, [next_time, next_node])
    return DP


import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N, M, X = map(int, input().split())
town_map1 = [[] for _ in range(N+1)]
town_map2 = [[] for _ in range(N+1)]
INF = 10**6 # 10,000*100

for _ in range(M):
    x1, x2, x3 = map(int, input().split())
    town_map1[x1].append([x2, x3]) # 원래 그래프
    town_map2[x2].append([x1, x3]) # 역 그래프(문제의 핵심)

result1 = dijkstra(X, town_map1)
result2 = dijkstra(X, town_map2)

print(max([i+j for i, j in zip(result1[1:], result2[1:])]))