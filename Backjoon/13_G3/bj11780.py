# 11780. 플로이드 2

from sys import stdin


def floyd():
    for k in range(N):  # 경유지
        for i in range(N):  # 출발지
            if i == k: continue  # 출발지와 경유지가 같으면 돌 필요 없음
            for j in range(N):  # 도착지
                if i == j: continue  # 출발지와 도착지가 같으면 돌 필요 없음
                if DP[i][j] > DP[i][k] + DP[k][j]:
                    DP[i][j] = DP[i][k] + DP[k][j]
                    grp[i*N+j] = grp[i*N+k] + grp[k*N+j][1:]  # 거리가 갱신될 때, 경로도 갱신


input = stdin.readline
N, M = int(input()), int(input())

INF = 10**7
DP = [[INF] * (N) for _ in range(N)]
grp = {i: [] for i in range(N*N)}  # 경로를 저장할 딕셔너리(i 계산은 (행*N + 열))

for _ in range(M):
    i, j, c = map(int, input().split())
    if DP[i-1][j-1] > c:
        DP[i-1][j-1] = c
        grp[(i-1)*N+(j-1)] = [i, j]  # 경로도 갱신

floyd()

for row in DP:
    for i in range(N):  # INF => 0 변환
        if row[i] == INF:
            row[i] = 0
    print(*row)

for val in grp.values():
    print(len(val), *val)  # 0도 그냥 출력됨
