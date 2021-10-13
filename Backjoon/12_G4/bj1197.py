# 1197. 최소 스패닝 트리

# MST에서는 Kruscal 알고리즘, Prim 알고리즘이 존재
# 간선이 적다면 Kruscal을 간선이 많다면 Prim 알고리즘
# Kruscal은 가중치를 기준으로 정렬해야 하기 때문!

# 방법1. Kruscal(빠름)
from sys import stdin


def find(x):  # 루트 노드를 찾는 함수
    if p[x] < 0: return x  # 음수인 경우 루트 노드
    p[x] = find(p[x])
    return p[x]


def union(x, y):  # 두 트리를 합치는 함수
    x, y = find(x), find(y)

    if x != y:  # 루트 노드가 다른 경우
        if p[x] <= p[y]:
            p[x] += p[y]
            p[y] = x
        else:
            p[y] += p[x]
            p[x] = y
        return True
    return False


input = stdin.readline
V, E = map(int, input().split())

p = [-1] * (V+1)  # 초기는 모두 루트 노드로 설정(음수 => 루트)
grp = [list(map(int, input().split())) for _ in range(E)]
grp.sort(key=lambda x: x[2])  # 가중치 순으로 정렬

ans = cnt = 0  # 최종 결과, 계산된 간선의 개수
for a, b, c in grp:
    if union(a, b):  # 루트 노드가 다른 경우(즉 사이클이 아닌 경우)
        cnt += 1
        ans += c
        if cnt == V-1: break  # V-1개의 간선을 확인하면 종료

print(ans)


# 방법2. Prim(느림)
# from sys import stdin
# from heapq import heappush, heappop


# def bfs(s):
#     global ans
#     cnt = 0  # 계산된 노드의 개수
#     q = [(0, s)]  # (가중치, 노드)

#     while q:
#         d, a = heappop(q)
#         if cnt == V: break  # 모든 노드를 확인한 경우

#         if not vst[a]:  # 방문한 적 없는 노드인 경우
#             vst[a] = True
#             ans += d
#             cnt += 1
#             for k, v in grp[a].items():
#                 heappush(q, (v, k))


# input = stdin.readline
# V, E = map(int, input().split())

# vst = [False] * (V+1)  # 방문 기록
# grp = [{} for _ in range(V+1)]
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     if b in grp[a]:  # 이미 있는 값인 경우 최솟값으로 갱신
#         grp[a][b] = min(grp[a][b], c)
#         grp[b][a] = min(grp[b][a], c)
#     else:  # 새로운 값인 경우
#         grp[a][b] = c
#         grp[b][a] = c

# ans = 0
# bfs(1)  # 시작 노드는 임의 지정
# print(ans)
