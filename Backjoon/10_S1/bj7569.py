# 7569. 토마토 

def bfs():
    bfs_list = set(list(ripe_tomato)) # 방문한 토마토 좌표가 저장될 공간
    cnt = 0 # 카운팅을 위한 변수
    
    h_init = ripe_tomato[-1][0] # 높이 초기값 저장할 변수(카운팅 기준을 잡기 위해)
    n_init = ripe_tomato[-1][1] # 행 초기값 저장할 변수
    m_init = ripe_tomato[-1][2] # 열 초기값 저장할 변수

    while ripe_tomato: # 숙성된 토마토 좌표가 없어질 때까지 반복
        h, n, m = ripe_tomato.popleft() # 가장 왼쪽에 저장된 좌표 받기
        for h_g, n_g, m_g in [(h-1, n, m), (h+1, n, m), (h, n-1, m), (h, n+1, m), (h, n, m-1), (h, n, m+1)]: # 윗층, 아랫층, 아래, 위, 왼쪽, 오른쪽 
            if farms[h_g][n_g][m_g] == 0 and (h_g, n_g, m_g) not in bfs_list: # 해당 좌표가 비숙성 토마토 and 방문한 적 없는 경우
                ripe_tomato.append(((h_g, n_g, m_g))) # 숙성된 토마토 좌표를 저장
                bfs_list.add((h_g, n_g, m_g)) # 방문한 좌표를 기록
        
        if h == h_init and n == n_init and m == m_init: # 만약 초기 좌표와 같은 경우
            if ripe_tomato: # 숙성된 토마토 좌표가 남아 있는 경우
                cnt += 1 # 카운팅 +1
                h_init = ripe_tomato[-1][0] # 높이 초기값 갱신
                n_init = ripe_tomato[-1][1] # 행 초기값 갱신
                m_init = ripe_tomato[-1][2] # 열 초기값 갱신
            else: # 숙성된 토마토 좌표가 남아 있지 않은 경우
                if len(bfs_list) == len(raw_tomato): # 전체 토마토 갯수 == 방문한 토마토 갯수인 경우
                    return cnt # 카운팅 반환
                return -1 # 아닌 경우(벽에 막혀서 못 가는 경우가 있는 것)

import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split()) # 열, 행, 높이 순서로 입력 받는 것
farms = [[[-1] * (M+2)] * (N+2)] + [[[] for _ in range(N+2)] for _ in range(H)] + [[[-1] * (M+2)] * (N+2)] # 3차원 토마토 농장 구현(입력 받을 공간은 공백([])으로 / 가두리도 만듬 -1로)
ripe_tomato = deque() # 숙성된 토마토 좌표를 저장(앞에서부터 pop을 해야하므로 deque이용)
raw_tomato = set() # 전체 토마토를 저장(cnt를 반환할지 -1을 반환할지 판별(길이로)하기 위함이므로 set 이용)

for h in range(1, H+1): # 높이 반복(입력 받을 높이만 -> 범위 1~H)
    for n in range(0, N+2): # 행 반복(0~(N+1)까지 다 반복함 -> 위에서 farms 구현할 때, 입력 받을 공간에서 가두리 못 만들었으므로 0과 (N+1)도 포함)
        if n in range(1, N+1): # 0~N일때 -> 입력(토마토) 받는 값
            farms[h][n] = [-1] + list(map(int, input().split())) + [-1] # 양 끝은 이동 불가능하므로 [-1]을 더해줌(이렇게 하면 나중에 범위 문제 편해짐)

            for m in range(1, M+1): # 숙성된 토마토와 비숙성 토마토 위치를 파악하기 위해
                if farms[h][n][m] == 1: # 숙성된 토마토일 경우
                    ripe_tomato.append(((h, n, m))) # 높이, 행, 열 순서의 좌표로 저장
                    raw_tomato.add((h, n, m)) # 전체 토마토 길이를 알기 위해 숙성된 토마토 좌표 저장(갯수로만 저장해도 상관 없었을 것 같음)

                if farms[h][n][m] == 0: # 비숙성 토마토일 경우
                    raw_tomato.add((h, n, m)) # 전체 토마토 길이를 알기 위해 숙성된 토마토 좌표 저장

        else: # 0, N+1일때 -> 가두리 구현
            farms[h][n] = [-1] * (M+2)

if ripe_tomato: # 숙성된 토마토가 있는 경우
    print(bfs())
else: # 숙성된 토마토가 없는 경우(히든 케이스...)
    print(-1)