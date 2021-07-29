# 18111. 마인크래프트(pyp3)

def minecraft(mine_map, blocks):
    best_time = sys.maxsize # 최대값 저장
    height = 0

    for i in range(min(mine_map), max(mine_map) + 1): # 설정 높이(mine_map의 최소 ~ 최대)
        # time = sum(list(map(lambda x: abs(x - i) * 2 if x >= i else abs(x - i), mine_map))) 방법은 좋은데 시간이 오래 걸릴 듯?
        time = 0
        block = blocks # 원본 blocks 값이 필요함
        for j in range(len(mine_map)): # mine_map을 반복
            if mine_map[j] >= i: # 블럭 높이가 설정 높이보다 높은 경우
                time += (mine_map[j] - i) * 2
                block += mine_map[j] - i # 블럭은 재활용 가능하므로 더해줘야 함
            else: # 블럭 높이가 설정 높이보다 낮은 경우
                time += (i - mine_map[j])
                block -= i - mine_map[j]
        
        if block >= 0 and time <= best_time: # block이 0보다 작거나, 기존 best_time보다 큰 경우는 거름
            best_time = time
            height = i
    
    return best_time, height

import sys

input = sys.stdin.readline

N, M, B = list(map(int, input().split()))
mine_world = []

for i in range(N):
    mine_world.append(list(map(int, input().split())))

mine_world = sum(mine_world, []) # 2차원 리스트 -> 1차원 리스트
time, height = minecraft(mine_world, B)

print(time, height)