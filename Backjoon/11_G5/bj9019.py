# 9019. DSLR(pypy3)

def bfs():
    bfs_list[A] = True # 첫 번째 수 True로
    visted_list = deque([(A, '')]) # (현재 숫자, 계산해 온 값)의 구조를 저장

    while visted_list:
        value, cal = visted_list.popleft()

        if value == B: # B에 도달한 경우
            return cal # 계산해 온 값인 cal 반환

        nexts = [(value*2%10000, 'D'),
                 ((value-1)%10000, 'S'),
                 (10*(value%1000) + value//1000, 'L'),
                 (1000*(value % 10) + value//10, 'R')
                 ] # 이동할 숫자 리스트('D', 'S' 연산 방법 기억하기)
        
        if len(set(str(value).rjust(4, '0'))) == 1: # 같은 숫자인 경우(굳이 'L', 'R'의 연산 수행할 필요 없음)
            for next_value, next_cal in nexts[:2]: # 'D', 'S'의 연산만 수행
                if  not bfs_list[next_value]: # 방문한 적 없는 경우
                    bfs_list[next_value] = True # True로 변환(방문했으므로)
                    visted_list.append((next_value, cal + next_cal))

        else: # 아닌 경우이므로 모든 숫자 리스트 수행
            for next_value, next_cal in nexts: # 'D', 'S', 'R', 'L' 모두 수행
                if not bfs_list[next_value]: # 방문한 적 없는 경우
                    bfs_list[next_value] = True # True로 변환(방문했으므로)
                    visted_list.append((next_value, cal + next_cal))

import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for i in range(T):
    bfs_list = [False] * 10000 # 시간 단축의 핵심(기존처럼 bfs.append() 방식은 느림 // 범위가 주어져 있다면 무조건 이렇게)
    A, B = map(int, input().split())
    print(bfs())