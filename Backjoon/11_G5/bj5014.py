# 5014. 스타트링크

from sys import stdin
from collections import deque


def bfs():
    q = deque([(S, 0)])  # 층, 이동 횟수
    v[S] = 1

    while q:
        n, c = q.popleft()
        if n == G: return c
        
        u, d = n + U, n - D
        if u <= F and not v[u]:  # 위로 가는 경우(for문보다 조건 분기가 더 빠름)
            v[u] = 1
            q.append((u, c+1))
        if d > 0 and not v[d]:
            v[d] = 1
            q.append((d, c+1))
    return 'use the stairs'  # 답을 못 찾은 경우


input = stdin.readline
F, S, G, U, D = map(int, input().split())

v = [0] * (F+1)
print(bfs())
