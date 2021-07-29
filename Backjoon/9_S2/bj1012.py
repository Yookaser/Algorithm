# 1012. 유기농 배추

def cabbage_farm(cabbage, row, col): # 해당 함수는 조건에 맞는 cabbage의 값을 0으로 바꾸는 역할
    cabbage[row][col] = 0 # 해당 값 초기화

    if (row - 1) in range(0, M) and cabbage[row - 1][col]: # 왼쪽으로 진행
        cabbage_farm(cabbage, row - 1, col)
    if (row + 1) in range(0, M) and cabbage[row + 1][col]: # 오른쪽으로 진행
        cabbage_farm(cabbage, row + 1, col)
    if (col - 1) in range(0, N) and cabbage[row][col - 1]: # 위쪽으로 진행
        cabbage_farm(cabbage, row, col - 1)
    if (col + 1) in range(0, N) and cabbage[row][col + 1]: # 아래쪽으로 진행
        cabbage_farm(cabbage, row, col + 1)

    return None # return은 큰 의미 없음

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())

for i in range(T):
    M, N, K = list(map(int, input().split()))
    cabbage = [[0] * N for _ in range(M)]
    count = 0
    
    for j in range(K): # 배추 위치 확인 후 심기(0 -> 1)
        x, y = list(map(int, input().split()))
        cabbage[x][y] = 1

    for i in range(M):
        for j in range(N):
            if cabbage[i][j] == 1: # 배추가 심어진 경우
                cabbage_farm(cabbage, i, j)
                count += 1

    print(count)