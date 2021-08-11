# 11660. 구간 합 구하기 5

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0] * (N+1)] + [[] for _ in range(N)]

for i in range(1, N+1):
    arr[i] = [0] + list(map(int, input().split()))

DP = [[0] * (N+1) for _ in range(N+1)] # 2차원으로 구간합을 저장함(인덱스 오류를 방지하기 위해 왼쪽, 위쪽 테두리 0으로)

for i in range(N):
    for j in range(N):
        DP[i+1][j+1] += (DP[i+1][j] + DP[i][j+1]) - DP[i][j] + arr[i+1][j+1] # 식은 한 번 DP 출력해보고 생각해볼 것

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1]) # 식은 한 번 DP 출력해보고 생각해볼 것