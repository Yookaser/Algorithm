# 9465. 스티커

def sticker(arr, N):
    if N == 1:
        return max(arr[0][0], arr[1][0])
    elif N == 2:
        return max(arr[0][0] + arr[1][1], arr[0][1] + arr[1][0])

    DP[0] = max(arr[0][0], arr[1][0])
    DP[1] = max(arr[0][0] + arr[1][1], arr[0][1] + arr[1][0])

    for i in range(2, N):
        DP[i] = max(DP[i-2] + max(arr[0][i], arr[1][i]),
                    DP[i-3] + arr[0][i-2] + arr[1][i-1] + arr[0][i],
                    DP[i-3] + arr[1][i-2] + arr[0][i-1] + arr[1][i]
                    )

    return DP[-1]

import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    DP = [0] * N
    arr = [list(map(int, input().split())) for _ in range(2)]
    print(sticker(arr, N))


'''
DP[i] = max(DP[i-3] + arr[0][i-2] + arr[1][i-1] + arr[0][i], 
                    DP[i-3] + arr[1][i-2] + arr[0][i-1] + arr[1][i],
                    DP[i-3] + arr[0][i-2] + arr[1][i], 
                    DP[i-3] + arr[1][i-2] + arr[0][i]
                    )
'''