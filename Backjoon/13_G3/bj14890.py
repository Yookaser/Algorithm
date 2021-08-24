# 14890. 경사로

def row_ramps(rc, way, direc='row'):  # row 또는 col 인덱스 번호, 배열, 행 또는 열
    temp = []  # 좌표 저장 리스트
    for idx in range(N-1):
        if abs(way[idx] - way[idx+1]) > 1:  # 인접 요소가 차이가 2이상인 경우
            return False

        if way[idx] - way[idx+1] == 1:  # 1인 경우(현재 인덱스가 더 큰 값임)
            for i in range(idx+1, idx+L+1):  # 뒤 L 칸만큼 검사 진행
                if direc == 'row' and i < N and way[idx+1] == way[i] and (rc, i) not in temp:  # 행 / 범위 내 / 같은 값 / 방문 x인 경우
                    temp.append((rc, i))
                elif direc == 'col' and i < N and way[idx+1] == way[i] and (i, rc) not in temp:  # 열 / 범위 내 / 같은 값 / 방문 x인 경우
                    temp.append((i, rc))
                else:
                    return False
        
        elif way[idx] - way[idx+1] == -1:  # -1인 경우(현재 인덱스가 작은 값임)
            for i in range(idx, idx-L, -1): # 앞의 L칸만큼 검사 진행(이때 자기 자신이 포함됨)
                if direc == 'row' and i > -1 and way[idx] == way[i] and (rc, i) not in temp:  # 행 / 범위 내 / 같은 값 / 방문 x인 경우
                    temp.append((rc, i))
                elif direc == 'col' and i > -1 and way[idx] == way[i] and (i, rc) not in temp:  # 열 / 범위 내 / 같은 값 / 방문 x인 경우
                    temp.append((i, rc))
                else:
                    return False
    return True


import sys

input = sys.stdin.readline
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

for idx, row in enumerate(arr):  # 행 계산
    if row_ramps(idx, row, 'row'):
        result += 1

for idx, col in enumerate(zip(*arr)):  # 열 계산
    if row_ramps(idx, col, 'col'):
        result += 1

print(result)