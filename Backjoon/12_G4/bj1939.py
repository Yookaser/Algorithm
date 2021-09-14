# 1939. 중량 제한

from sys import stdin
from collections import deque


def bfs(A, B, w):
    q = deque([A])
    visited = set([A])

    while q:
        n = q.popleft()
        if n == B:  # 목적지에 도착한 경우
            return True
        for nn, nw in grf[n].items():
            if nn not in visited and nw >= w:  # 방문한 적 없고 중량 제한에 안 걸리는 경우
                q.append(nn)
                visited.add(nn)
        print(visited)
    return False  # 목적지에 도착하지 못한 경우


input = stdin.readline
N, M = map(int, input().split())
grf = [{} for _ in range(N+1)]

s, e = 1, 0  # 이분 탐색을 위한
for _ in range(M):  # 양방향임을 명시할 것
    A, B, C = map(int, input().split())
    e = max(e, C)
    if grf[A].get(B):  # 값이 이미 있는 경우 최대값으로 갱신
        grf[A][B] = max(grf[A][B], C)
        grf[B][A] = max(grf[B][A], C)
    else:
        grf[A][B] = C
        grf[B][A] = C
print(grf)
A, B = map(int, input().split())

ans = 1
while s <= e:  # 이분 탐색
    mid = (s+e) // 2
    if bfs(A, B, mid):
        s = mid + 1
        ans = mid
    else:
        e = mid - 1

print(ans)
