# 9370. 미확인 도착지

from sys import stdin
from heapq import heappush, heappop


def dijkstra(x):
    q = [(0, x)]
    DP = [10**7] * (N+1)  # 문제 상 최대값 1,000 * 2,000
    DP[x] = 0

    while q:
        d, n = heappop(q)

        if DP[n] < d:
            continue

        for nn, nd in grp[n].items():
            x = d + nd
            if DP[nn] > x:
                DP[nn] = x
                heappush(q, (x, nn))
    return DP


input = stdin.readline
T = int(input())
for _ in range(T):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())
    grp = [{} for _ in range(N+1)]

    for _ in range(M):
        a, b, d = map(int, input().split())
        grp[a][b] = d
        grp[b][a] = d

    t = [int(input()) for _ in range(T)]
    
    S_DP = dijkstra(S)  # 시작점에서의 다익스트라 계산
    C_DP = dijkstra(G) if S_DP[G] > S_DP[H] else dijkstra(H)  # 시작점과 더 먼 곳에서 다익스트라 계산

    ans = []
    for i in t:
        if S_DP[i] == min(S_DP[G], S_DP[H]) + grp[G][H] + C_DP[i]:  # (시작점-목적지) == (시작점-교차로1-교차로2-목적지)
            ans.append(i)

    print(*sorted(ans))
