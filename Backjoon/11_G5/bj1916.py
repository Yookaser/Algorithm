# 1916. 최소비용 구하기

def dijkstra(start):
    DP[start] = 0 # 시작 비용 0으로
    heap = []
    heapq.heappush(heap, [0, start]) # heapq는 작은 것 순서대로 정렬함(따라서 (비용, node)에서 순서 바꾸면 안됨)
    while heap: # heap이 없을 때까지
        node_cost, node  = heapq.heappop(heap)
        if DP[node] < node_cost: # 시작지점에서 해당 node값으로 이동하는 비용이 기존 DP값보다 큰 경우
            continue # 아래 for문 안 돌음
        for next, cost in bus[node]: # 해당 node에서 이동할 수 있는 것 반복
            next_cost = node_cost + cost # 현재 노드까지 비용 + 다음 노드로 이동 비용
            if DP[next] > next_cost: # 현재 노드에서 이동한 비용이 다음 노드의 비용보다 작은 경우
                DP[next] = next_cost # 비용 변경
                heapq.heappush(heap, [next_cost, next]) # 다음 노드 저장

import sys
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]
DP = [10**8 for _ in range(N+1)] # 비용을 저장하는데 다익스트라 알고리즘이므로 최대값으로 초기화(최대 node 1000개, 최대 비용 100000이므로 10*8으로 설정)

for _ in range(M):
    x, y, c = map(int, input().split())
    bus[x].append([y, c]) # 다익스트라를 위해 x에 [y, c]를 저장

first, last = map(int, input().split())

dijkstra(first) # 시작 지점부터 시작
print(DP[last])