# 17219. 비밀번호 찾기

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
hp_pwd = {} # 홈페이지와 비밀번호가 들어갈 공간(자료를 입력 받고 반환하면 되므로 딕셔너리 선언)

for _ in range(N):
    homepage, password = input().split()
    hp_pwd[homepage] = password

for _ in range(M):
    print(hp_pwd[input().rstrip()])