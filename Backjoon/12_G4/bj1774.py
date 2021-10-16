# 1774. 우주신과의 교감

from sys import stdin
from heapq import heappush, heappop


def dist(x, y):  # 거리를 구하는 함수
    return (abs(x[0]-y[0])**2+(x[1]-y[1])**2)**0.5


def find(x):  # 루트 노드를 찾는 함수
    if p[x] < 0: return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):  # 합병 함수
    x, y = find(x), find(y)

    if x != y:
        if p[x] <= p[y]:
            p[x] += p[y]
            p[y] = x
        else:
            p[y] += p[x]
            p[x] = y
        return True
    return False


input = stdin.readline
N, M = map(int, input().split())
A = [0] + [tuple(map(int, input().split())) for _ in range(N)]

ans = cnt = 0
p = [-1] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    if union(a, b):  # a, b의 루트 노드가 다른 경우 cnt +1
        cnt += 1

grp = []
for i in range(1, N+1):  # 없는 노드만이 아닌 모든 노드의 거리를 구해야 함
    for j in range(i+1, N+1):
        heappush(grp, (dist(A[i], A[j]), i, j))  # 정렬보다 heapq를 이용하는 것이 빨랐음


while cnt != N - 1:
    d, i, j = heappop(grp)
    if union(i, j):
        cnt += 1
        ans += d

print(format(ans, '.2f'))
