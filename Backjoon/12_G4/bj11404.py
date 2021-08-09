# 11404. 플로이드

def floyd():
    for k in range(N): # 경유지
        for i in range(N): # 출발지
            for j in range(N): # 도착지
                if i != j:
                    DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j]) # 직진과 경유지를 거친 값 중 더 적은 값을 선택

import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
maxi = 10**9 # 대략적인 값으로 설정함
DP = [[maxi if i != j else 0 for i in range(N)] for j in range(N)] # 행과 열이 같은 경우를 제외하고, maxi로

for _ in range(M):
    a, b, c = map(int, input().split())
    DP[a-1][b-1] = min(DP[a-1][b-1], c)

floyd()

for x in range(N):
    for y in range(N):
        if DP[x][y] != maxi:
            print(DP[x][y], end=' ')
        else:
            print(0, end=' ')
    print()