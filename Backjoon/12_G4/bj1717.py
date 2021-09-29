# 1717. 집합의 표현

# 방법1. 유니온 파인드1
from sys import stdin


def find(x):  # 루트 노드를 찾는 함수
    if p[x] < 0: return x  # 음수인 경우 루트 노드
    p[x] = find(p[x])
    return p[x]


def union(x, y):  # 두 트리를 합치는 함수
    x = find(x)
    y = find(y)
    if x != y:  # 루트 노드가 같은 경우는 이미 같은 트리이므로 무시
        if p[x] < p[y]:  # 더 작은 트리를 합치기 위함(더 음수일수록 더 큰 트리임)
            p[x] += p[y]  # 루트 노드
            p[y] = x  # 합쳐지는 작은 트리
        else:
            p[y] += p[x]
            p[x] = y


input = stdin.readline
N, M = map(int, input().split())
p = [-1] * (N+1)  # 초기는 모두 루트 노드로 설정(음수 => 루트)

for _ in range(M):
    j, a, b = map(int, input().split())
    if j:
        print("YES" if find(a) == find(b) else "NO")
    else:
        union(a, b)
   
# 방법2. 유니온 파인드2(조금 더 느림)
# from sys import stdin, setrecursionlimit


# def find(x):  # 루트 노드를 찾는 함수
#     if x == p[x]: return x  # 루트 노드인 경우
#     p[x] = find(p[x])
#     return p[x]


# def union(x, y):  # 두 트리를 합치는 함수
#     x = find(x)
#     y = find(y)
#     if x < y:  # 더 작은 노드 번호를 합침(더 작은 트리가 아님 => 느린 원인)
#         p[y] = x
#     else:
#         p[x] = y


# input = stdin.readline
# setrecursionlimit(10**6)
# N, M = map(int, input().split())
# p = [i for i in range(N+1)]  # 초기는 모두 루트 노드로 설정(요소값은 루트 노드를 가리킴)

# for _ in range(M):
#     j, a, b = map(int, input().split())

#     if j:
#         if find(a) == find(b):
#             print('YES')
#         else:
#             print('NO')
#     else:
#         union(a, b)
