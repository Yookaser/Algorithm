# 17404. RGB거리

from sys import stdin


input = stdin.readline
N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
DP = [[0] * 3 for _ in range(N)]

ans = INF = 10**10
for c in range(3):  # 3색 반복
    for i in range(3):  # 초기값 지정
        if c == i: DP[0][i] = A[0][i]
        else: DP[0][i] = INF
    
    for i in range(1, N):  # 색이 안겹치는 방향으로 갱신
        DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + A[i][0]
        DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + A[i][1]
        DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + A[i][2]
    
    for i in range(3):  # 최솟값 찾기
        if c != i and ans > DP[-1][i]:
            ans = DP[-1][i]

print(ans)
    