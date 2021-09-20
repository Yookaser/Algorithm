# 1707. 이분 그래프

from sys import stdin
from collections import deque


def bfs(s):
    q = deque([s])
    DP[s] = 1  # 들어온 값은 1로 통일

    while q:
        v = q.popleft()

        for nv in g[v]:
            if DP[nv] == 0:  # 아직 색이 없는 경우
                DP[nv] = -DP[v]  # 1 => -1, -1 => 1
                q.append(nv)
            elif DP[nv] == DP[v]:  # 간선끼리 색이 같은 경우
                return True
    return False
             

input = stdin.readline
T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    g = [[] for _ in range(V+1)]  # 내부 요소가 집합보다 리스트인 경우가 더 빨랐음

    for i in range(E):  # 양방향 적용
        n, m = map(int, input().split())
        g[n].append(m)
        g[m].append(n)
    
    DP = [0] * (V+1)
    for i in range(1, V+1):
        if DP[i] == 0:  # 아직 색이 없는 경우
            if bfs(i):
                print('NO')
                break
    else:
        print('YES')
