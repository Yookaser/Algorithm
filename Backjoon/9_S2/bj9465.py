# 9465. 스티커

# 방법1. DP(최적화 필요)
def sticker(arr, N):
    if N == 1: # 1인 경우
        return max(arr[0][0], arr[1][0])
    elif N == 2: # 2인 경우
        return max(arr[0][0] + arr[1][1], arr[0][1] + arr[1][0])

    # 필요 DP값 미리 저장
    DP[0][0] = arr[0][0]
    DP[0][1] = arr[1][0]
    DP[1][0] = arr[1][0] + arr[0][1]
    DP[1][1] = arr[0][0] + arr[1][1]

    for i in range(2, N):
        DP[i][0] = max(DP[i-2][1] + arr[0][i], DP[i-1][1] + arr[0][i]) # i번째 0번 칸으로 오기 위한 가지수 2개 중 최대
        DP[i][1] = max(DP[i-2][0] + arr[1][i], DP[i-1][0] + arr[1][i]) # i번째 1번 칸으로 오기 위한 가지수 2개 중 최대

    return max(DP[-1][0], DP[-1][1]) # 마지막 두 값 중 큰 값 반환

import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    DP = [[0, 0] for _ in range(N)] # DP를 각 칸에 2개로 나눔(이 문제의 핵심)
    arr = [list(map(int, input().split())) for _ in range(2)]
    print(sticker(arr, N))