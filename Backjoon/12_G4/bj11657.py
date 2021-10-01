# 11657. 타임머신

from sys import stdin


def bfs(s):
    q = [s]
    v = set()

    while q:  # 1에서 방문 가능한 집합 생성을 위함
        n = q.pop()

        for nn, d in grp[n].items():
            if nn not in v:
                v.add(nn)
                q.append(nn)

    DP = [INF] * (N+1)
    DP[s] = 0
    for _ in range(N):
        flag = False
        
        for n in range(1, N+1):
            for nn, d in grp[n].items():
                if DP[nn] > DP[n] + d:  # 갱신 가능한 경우
                    DP[nn] = DP[n] + d
                    if n in v:  # 갱신 가능했는데 n이 1에서 방문 가능한 노드인 경우
                        flag= True

        if not flag:  # 갱신이 되지 않은 경우(음의 사이클이 없는 것)
            for i in range(2, N+1):
                if i not in v or DP[i] == INF:  # 1에서 방문 가능하지 않은 경우 or 갱신되지 않은 경우
                    DP[i] = -1
            return DP[2:]
    return [-1]  # 음의 사이클이 존재한 경우


input = stdin.readline
N, M = map(int, input().split())
grp = [{} for _ in range(N+1)]
INF = 10**8

for _ in range(M):
    A, B, C = map(int, input().split())
    if grp[A].get(B):
        grp[A][B] = min(grp[A][B], C)
    else:
        grp[A][B] = C

ans = bfs(1)
print(*ans, sep='\n')
