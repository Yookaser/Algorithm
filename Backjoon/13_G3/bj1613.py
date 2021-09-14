# 1613. 역사

# 방법1. 플로이드(pypy3)
from sys import stdin


def floyd():
    for k in range(N):  # 경유
        for i in range(N):  # 시작
            for j in range(N):  # 끝
                if DP[i][k] == DP[k][j] == 1:  # 경유해서 갈 수 있는 경우
                    DP[i][j] = 1

input = stdin.readline
N, K = map(int, input().split())
DP = [[0] * N for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    DP[a-1][b-1] = 1  # 양방향이지만, 문제 조건과 로직상 단방향으로 추가

floyd()

S = int(input())
for _ in range(S):
    a, b = map(int, input().split())
    if DP[a-1][b-1]:  # 1인 경우
        print(-1)
    elif DP[b-1][a-1]:  # 1인 경우
        print(1)
    else:
        print(0)

# 방법2. bfs
# from sys import stdin
# from collections import deque


# def bfs(s):
#     q = deque([s])

#     while q:
#         n = q.popleft()

#         for x in grf[n]:
#             if not DP[s][x]:  # 시작 노드를 기준으로 삼아야 함
#                 DP[s][x] = 1
#                 q.append(x)


# input = stdin.readline
# N, K = map(int, input().split())
# grf = [[] for _ in range(N+1)]
# DP = [[0] * (N+1) for _ in range(N+1)]

# for _ in range(K):
#     a, b = map(int, input().split())
#     grf[a].append(b)  # 양방향이지만, 문제 조건과 로직상 단방향으로 추가

# for i in range(1, N+1):  # 1부터 N 노드 모두 순회
#     bfs(i)

# S = int(input())
# for _ in range(S):
#     a, b = map(int, input().split())
#     if DP[a][b]:  # 1인 경우
#         print(-1)
#     elif DP[b][a]:  # 1인 경우
#         print(+1)
#     else:  # 둘 다 1이 아니면 알 수 없음
#         print(0)
