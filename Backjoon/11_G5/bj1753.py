# 1753. 최단경로

# x에서 y까지 여러 간선이 있으면 가장 짧은 것만 필요함
# 그래서 시간을 단축을 위해 dijstra 함수 전에 미리 최소 간선만 node_map에 저장하도록 했으나 실패함(딕셔너리로 함)
# 이렇게 단축시키는 것 보다 그냥 최소힙을 이용하여 'if DP[node] < node_cost:'에서 거르는게 더 빨랐음
def dijstra(start):
    DP[start] = 0
    heap = []
    heappush(heap, [0, start]) # 비용이 작은 것순으로 정렬함(따라서 (비용, node)에서 순서 바꾸면 안됨)

    while heap:
        node_cost, node = heappop(heap)
        if DP[node] < node_cost: # 시작지점에서 해당 node값으로 이동하는 비용이 기존 DP값보다 큰 경우
            continue # 아래 for문 안 돌음
        for next, cost in node_map[node]: # 해당 node에서 이동할 수 있는 것 반복(연결 리스트)
            next_cost = node_cost + cost # 현재 노드까지 비용 + 다음 노드로 이동 비용
            if DP[next] > next_cost: # 현재 노드에서 이동한 비용이 다음 노드의 비용보다 작은 경우
                DP[next] = next_cost # 비용 변경
                heappush(heap, [next_cost, next]) # 다음 노드 저장

import sys
from heapq import heappush, heappop # 시간을 조금이라도 단축시키기 위해 사용할 기능만 불러옴

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
node_map = [[] for _ in range(V+1)]
DP = [10**6 for _ in range(V+1)] # 비용을 저장하는데 다익스트라 알고리즘이므로 최대값으로 초기화(최대 2*(10**5)이겠지만, 안전을 위해 10**6으로 설정)

for _ in range(E):
    x, y, c = map(int, input().split())
    node_map[x].append([y, c]) # 다익스트라를 위해 x에 [y, c]를 저장(메모리를 위해 연결값만 구현해야 함(연결 리스트))

dijstra(K)
for i in DP[1:]:
    if i == 10**6: # 답을 못 찾은 경우
        print('INF')
    else:
        print(i)