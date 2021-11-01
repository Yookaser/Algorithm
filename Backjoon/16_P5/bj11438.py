# 11438. LCA 2

import sys


def dfs(n, depth):  # 깊이를 탐색하기 위한 함수
    v[n], d[n] = 1, depth
    for nn in grp[n]:
        if v[nn]: continue
        p[nn][0] = n  # 첫 번째 조상만 저장
        dfs(nn, depth+1)


def lca(a, b):  # 공통 조상을 찾기 위한 함수
    if d[a] > d[b]: a, b = b, a  # b의 깊이를 더 크게 만듬

    for i in range(16, -1, -1):  # 두 노드의 깊이 맞춰주기
        if d[b] - d[a] >= (1<<i): b = p[b][i]
        if d[b] - d[a] == 0: break
    
    if a != b:
        for i in range(16, -1, -1):  # 두 노드의 공통 조상을 찾기(2**i번째 조상으로 접근)
            if p[a][i] != p[b][i]:
                a = p[a][i]
                b = p[b][i]
        return p[a][0]
    return a


sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
p = [[0] * 17 for _ in range(N+1)]  # 조상 저장(2**index번째 조상들을 모두 저장함)
d = [0] * (N+1)  # 깊이 저장
v = [0] * (N+1)  # 방문 저장
grp = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    grp[a].append(b)
    grp[b].append(a)

dfs(1, 0)
for i in range(1, 17):  # 조상의 높이 반복
    for j in range(1, N+1):  # 노드 반복
        if d[j] < (1<<i): continue  # 깊이보다 i가 커지면 pass
        p[j][i] = p[p[j][i-1]][i-1]  # i번째에 조상의 i-1번째를 저장하기

cache = dict()  # 메모이제이션을 위한 dict
M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    if (a, b) in cache: print(cache[(a, b)])
    else:
        cache[(a, b)] = cache[(b, a)] = lca(a, b)  # 반대 경우도 넣어줌(시간 단축의 핵심)
        print(cache[(a, b)])
