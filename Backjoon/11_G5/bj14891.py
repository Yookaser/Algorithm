# 14891. 톱니바퀴

import sys

input = sys.stdin.readline
gears = [list(map(int, input().rstrip())) for _ in range(4)]
rotation = [[2, 6] for _ in range(4)]  # 오른쪽 접합부 인덱스, 왼쪽 접합부 인덱스
result = 0  # 결과값 저장할 변수
K = int(input())

for _ in range(K):
    gear, direc = map(int, input().split())
    temp = [(gear-1, direc)]  # (기어 번호, 회전 방향)을 저장
    c_direc = direc  # 임시 방향 저장 변수
    for i in range(gear, 4):  # 자신보다 뒤의 톱니바퀴 반복
        c_direc *= -1  # 시계 방향 -> 반시계 방향 -> 시계 방향을 구현
        if gears[i-1][rotation[i-1][0]] != gears[i][rotation[i][1]]:  # 접합부의 극이 다른 경우
            temp.append((i, c_direc))  # 회전해야 하므로 (기어 번호, 회전 방향) 저장
        else:
            break
    c_direc = direc
    for i in range(gear-2, -1, -1):  # 자신보다 앞의 톱니바퀴 반복
        c_direc *= -1
        if gears[i+1][rotation[i+1][1]] != gears[i][rotation[i][0]]:
            temp.append((i, c_direc))
        else:
            break
    
    for i, j in temp:  # 저장했던 (기어번호, 회전방향)을 처리
        rotation[i][0] = (rotation[i][0]-j) % 8  # 1(시계 방향): 인덱스 작아짐, -1(반시계 방향): 인덱스 커짐
        rotation[i][1] = (rotation[i][1]-j) % 8

for i in range(4):
    if gears[i][(rotation[i][0]-2)%8] == 1:  # 12시가 S인 경우(12시 방향은 오른쪽 접합부에서 2칸 앞임)
        result += 2**i  # 문제 조건에 맞는 점수를 더함

print(result)