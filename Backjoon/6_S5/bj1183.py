# 1183. 약속

import sys

input = sys.stdin.readline

N = int(input())
differ_list = [] # abs(약속시간 - 도착시간)의 값을 저장할 공간

for _ in range(N):
    promise = list(map(int, input().split()))
    differ_list.append(promise[0] - promise[1])

if N % 2 == 1: # 만약 홀수라면 중앙값의 부호 역수가 최적의 T가 됨
    print(1)

else:
    differ_list.sort() # 만약 짝수라면 중앙값 2개 사이의 값들의 부호 역수들이 최적의 T가 됨
    result = abs(differ_list[N // 2 - 1] - differ_list[N // 2]) + 1
    print(result)