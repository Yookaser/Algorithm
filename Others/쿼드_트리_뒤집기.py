# 쿼드 트리 뒤집기 (https://algospot.com/judge/problem/read/QUADTREE)

def find_mid(arr): # 좌상, 우상, 좌하, 우하의 분기를 찾는 함수
    cnt = 0 # 카운팅
    result = [] # 결과
    confirm = [False, False, False] # 중복을 방지하기 위한 리스트

    for word in range(1, len(arr)):
        if arr[word] != 'x': # x가 아닌 경우
            cnt += 1 # 카운틴
        else: # x인 경우
            cnt -= 3 # 3개의 숫자가 더 나와야 하므로 -3
        if cnt == 1 and not confirm[0]: # 좌상과 우상의 구분점을 찾았고, 
            confirm[0] = True # 기록한 것으로 바꿈
            result.append(word+1) # 결과 저장
        if cnt == 2 and not confirm[1]:
            confirm[1] = True
            result.append(word+1)
        if cnt == 3 and not confirm[2]:
            confirm[2] = True
            result.append(word+1)
    return result


def tree_reverse(arr):
    if len(arr) == 1: # arr 길이가 1인 경우
        result.append(arr[0]) # 결과에 저장
        return
    else: # arr 길이가 1이 아닌 경우
        result.append('x') # 'x' 결과에 저장(무조건 x로 시작하게 되어있음)
        second, third, fourth = find_mid(arr) # 분기점 받기

        tree_reverse(arr[third:fourth]) # 좌하(상하 뒤집히므로 가장 먼저 나와야 함)
        tree_reverse(arr[fourth:]) # 우하(두번째로 나옴)
        tree_reverse(arr[1:second]) # 좌상(세번째로 나오고, 'x'를 빼줘야 하므로 범위 1부터)
        tree_reverse(arr[second:third]) # 우상(마지막)
        

import sys

input = sys.stdin.readline
N = int(input())

for i in range(N):
    result = []
    words = input().rstrip()
    tree_reverse(words)
    print(*result, sep='')