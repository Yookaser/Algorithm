# 2096. 내려가기

import sys

input = sys.stdin.readline
N = int(input())

point = list(map(int, input().split()))
DP_max, DP_min = [[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]]  # 2차원 리스트(0행, 1행 반복할 것)
DP_max[0], DP_min[0] = point[:], point[:]  # 시작은 0번째 행을 point 복사
cnt, i, j = 1, 1, 0  # 횟수 판별, dp 인덱스, 기존값 인덱스

while cnt < N:
    point = list(map(int, input().split()))

    DP_max[i][0] = max(DP_max[j][0], DP_max[j][1]) + point[0]  # 최대값 DP
    DP_max[i][1] = max(DP_max[j]) + point[1]
    DP_max[i][2] = max(DP_max[j][1], DP_max[j][2]) + point[2]

    DP_min[i][0] = min(DP_min[j][0], DP_min[j][1]) + point[0]  # 최소값 dp
    DP_min[i][1] = min(DP_min[j]) + point[1]
    DP_min[i][2] = min(DP_min[j][1], DP_min[j][2]) + point[2]

    i, j = (i - 1) % 2, (j - 1) % 2  # 인덱스 바꾸기(만약, (i, j)가 (1, 0) 이였으면, (0, 1)로 바꿔주는 것)
    cnt += 1  # 횟수 카운트

print(max(DP_max[j]), min(DP_min[j]))