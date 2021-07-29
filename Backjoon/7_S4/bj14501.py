# 14501. 퇴사

import sys

input = sys.stdin.readline

N = int(input())
times = [0] * (N + 1) # 소요 시간을 저장할 공간
pays = [0] * (N + 1) # 급여를 저장할 공간
my_pay = [0] * (N + 1) # 내가 받을 수 있는 금액을 저장할 공간(인덱스는 일자를 의미)

for i in range(1, N + 1):
    times[i], pays[i] = list(map(int, input().split()))
    
for i in range(1, N + 1):
    if (times[i] + i) <= (N + 1): # 기한 내에 상담을 끝낼 수 있는 경우
        my_pay[times[i] + i - 1] = max(my_pay[times[i] + i - 1], max(my_pay[:i]) + pays[i]) # max(상담이 끝난 날의 급여, 현재 일까지 가장 큰 급여 + 오늘 상담을 시작하면 받는 금액)

print(max(my_pay))