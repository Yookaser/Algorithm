# 11473. LCA

import sys


def dfs(n, depth):  # 깊이를 탐색하기 위한 함수
    v[n], d[n] = 1, depth
    for nn in grp[n]:
        if v[nn]: continue
        p[nn] = n
        dfs(nn, depth+1)


def lca(a, b):  # 공통 조상을 찾기 위한 함수
    while d[a] != d[b]:  # 두 노드의 깊이 맞춰주기
        if d[a] > d[b]: a = p[a]
        else: b = p[b]
    while a != b:  # 두 노드의 공통 조상을 찾기
        a = p[a]
        b = p[b]
    return a


sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
p = [0] * (N+1)  # 조상 저장
d = [0] * (N+1)  # 깊이 저장
v = [0] * (N+1)  # 방문 저장
grp = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    grp[a].append(b)
    grp[b].append(a)

dfs(1, 0)

cache = dict()  # 메모이제이션을 위한 dict
M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    if (a, b) in cache: print(cache[(a, b)])
    else:
        cache[(a, b)] = cache[(b, a)] = lca(a, b)  # 반대 경우도 넣어줌(시간 단축의 핵심)
        print(cache[(a, b)])
