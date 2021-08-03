# 11659. 구간 합 구하기4

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [0] + list(map(int, input().split())) # 인덱스를 맞추기 위해 인덱스 0 생성
pre_sum = [0] * (N+1) # 인덱스를 맞추기 위해 인덱스 0 생성

for i in range(1, N+1): # i-1이 필요하기 때문에 범위(1~N) 설정
    pre_sum[i] = pre_sum[i-1] + arr[i] # 미리 i번째까지의 합계를 계산

for _ in range(M):
    i, j = map(int, input().split())
    print(pre_sum[j] - pre_sum[i-1]) # j까지의 합계 - (i-1)까지의 합계로 i~j까지 합계를 구함(시간 복잡도 매우 낮아짐)