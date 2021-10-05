# 10217. KCM Travel

# 방법1. 다익스트라
from sys import stdin
from collections import deque


def dijkstra():
    DP = [[INF] * (M+1) for _ in range(N+1)]  # 행: 공항, 열: 비용, 값: 시간
    DP[1][0] = 0  # 초기값 0
    q = deque([(1,0,0)]) # 공항, 비용, 시간

    while q:
        n, c, d = q.popleft()

        if DP[n][c] < d: continue

        for nn, nc, nd in arr[n]:
            ic, id = c + nc, d + nd
            if ic > M or DP[nn][ic] <= id: continue  # 비용 초과 or 더 적은 시간이 이미 존재인 경우 pass
            q.append((nn, ic, id))

            for i in range(ic, M+1):
                if DP[nn][i] > id: DP[nn][i] = id
                else: break  # 뒤는 더 볼 필요가 없음

    return min(DP[N]) if min(DP[N]) != INF else 'Poor KCM'


input = stdin.readline
INF = 10**6
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        arr[u].append((v, c, d))

    print(dijkstra())

# 방법2. DP(느림)
# from sys import stdin


# input = stdin.readline
# T = int(input())
# INF = 10**6
# for _ in range(T):
#     N, M, K = map(int, input().split())
#     arr = [[] for _ in range(N+1)]
#     DP = [[INF] * (M+1) for _ in range(N+1)]  # 행: 공항, 열: 비용, 값: 시간
#     DP[1][0] = 0  # 초기값 0

#     for _ in range(K):
#         u, v, c, d = map(int, input().split())
#         arr[u].append((v, c, d))
    
#     for m in range(M+1):  # 비용만큼 반복
#         for n in range(1, N+1):  # 공항만큼 반복
#             if DP[n][m] != INF:  # 갱신된 적 없는 경우

#                 for v, c, d in arr[n]:
#                     if m + c <= M and DP[v][m+c] > DP[n][m] + d:  # 비용(M) 내이고 더 적은 경우
#                         DP[v][m+c] = DP[n][m] + d  # 갱신

#     print(min(DP[N]) if min(DP[N]) != INF else 'Poor KCM')
