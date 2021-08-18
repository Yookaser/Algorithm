# 1620. 나는야 포켓몬 마스터 이다솜

import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
poketmon_alpha = {} # 포켓몬 -> 숫자(딕셔너리 써야함! 리스트 매우 느림)
poketmon_digit = {} # 숫자 -> 포켓몬

for _ in range(N):
    poketmon = input().rstrip() # .rstrip() 안쓰면 뒤에 \n 붙음
    poketmon_alpha[poketmon] = _ + 1 # key: 포켓몬 이름, value: 도감 순서
    poketmon_digit[_ + 1] = poketmon # key: 도감 순서, value: 포켓몬 이름

for i in range(M):
    problem = input().rstrip()

    if problem.isdigit(): # .rstrip() 안쓰면 뒤에 \n 붙음
        print(poketmon_digit[int(problem)]) # 문자형으로 받으므로 int로 형변환 해야함
    else:
        print(poketmon_alpha[problem])