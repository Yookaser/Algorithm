# 14938. 서강 그라운드

# 방법1. 플로이드
import sys


def floyd():
    for k in range(N): # 경유지
        for i in range(N): # 출발지
            for j in range(N): # 도착지
                if i != j:
                    DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j]) # 직진과 경유지를 거친 값 중 더 적은 값을 선택


input = sys.stdin.readline
N, M, R = map(int, input().split())
t = list(map(int, input().split()))
maxi = 10**4  # 문제 조건 상 100*100이 최대이므로 10,000으로 설정
DP = [[maxi if i != j else 0 for i in range(N)] for j in range(N)]  # 자기 자신 외에는 최대로 설정

for i in range(R):  # 양방향이므로 둘 다 설정
    a, b, l = map(int, input().split())
    DP[a-1][b-1] = min(DP[a-1][b-1], l)
    DP[b-1][a-1] = min(DP[b-1][a-1], l)

floyd()

ans = [0] * N
for i in range(N):
    for j in range(N):
        if DP[i][j] <= M:  # i -> j의 거리가 M 이하인 경우
            ans[i] += t[j]

print(max(ans))

# 방법2. 다익스트라

# import sys
# from heapq import heappush, heappop


# def dijkstra(idx):
#     D = [maxi]*(N+1)
#     D[idx] = 0
#     q = []
#     heappush(q, (0, idx))  # 비용을 먼저 위치시켜서 최소힙 구현

#     while q:
#         c, n = heappop(q)
#         if D[n] < c:  # 비용이 더 작다면 밑에 실행할 필요가 없음
#             continue
        
#         for nn, nc in g[n].items():  # dict로 구현했으므로 itemps를 이용
#             cc = c + nc
#             if D[nn] > cc:
#                 D[nn] = cc
#                 heappush(q, (cc, nn))
    
#     res = 0
#     for i in range(1, N+1):  # 거리 확인
#         if D[i] <= M:
#             res += t[i]
#     return res


# input = sys.stdin.readline
# N, M, R = map(int, input().split())
# t = [0] + list(map(int, input().split()))  # 인덱스 맞추기 위해 0 추가
# g = [dict() for i in range(N+1)]
# maxi = 10**4  # 문제 조건 상 100*100이 최대이므로 10,000으로 설정

# for i in range(R):  # 양방향이므로 둘 다 설정
#     a, b, l = map(int, input().split())
#     g[a][b], g[b][a] = l, l

# ans = [0] * (N+1)
# for i in range(1, N+1):
#     ans[i] = dijkstra(i)  # i 번째 노드의 다익스트라 시행

# print(max(ans))
