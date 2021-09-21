# 11404. 플로이드

from sys import stdin


def floyd():
    for k in range(N): # 경유지
        for i in range(N): # 출발지
            if i == k: continue  # 출발지와 경유지가 같으면 돌 필요 없음
            for j in range(N): # 도착지
                if i == j: continue  # 출발지와 도착지가 같으면 돌 필요 없음
                if DP[i][j] > DP[i][k] + DP[k][j]:  # min보다 조건문 처리가 더 빨랐음(이유는 모르겠음)
                    DP[i][j] = DP[i][k] + DP[k][j]


input = stdin.readline
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
