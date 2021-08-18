# 3190. 뱀

def snake_game():
    x, y, cnt, dist = 1, 1, 0, 1 # 시작 x, 시작 y, 카운트, 시작 방향(우)
    snake = deque([(x, y)]) # 뱀의 몸이 있는 좌표를 저장

    while True:
        # print('# {} #'.format(cnt), x,y, snake)
        x += move[dist][0] # x 이동
        y += move[dist][1] # y 이동
        cnt += 1 # 카운트 +1

        if x < 1 or x > N or y < 1 or y > N or (x, y) in snake: # 벽을 부딪히거나 자신의 몸에 부딪힌 경우
            break
        
        snake.append((x, y)) # 머리가 먼저 움직이므로 일단 추가
        if [x, y] not in apple: # 사과가 없는 경우
            snake.popleft() # 꼬리 제거
        else: # 사과가 있는 경우
            apple.remove([x, y]) # 사과 제거

        if cnt in direction: # 해당 카운트가 방향에 있는 경우
            if direction[cnt] == 'D': # 오른쪽인 경우
                dist = (dist+1) % 4 # +1
            else:
                dist = (dist-1) % 4 # 음수 -1이 나오면 나머지 3이됨
    return cnt


import sys
from collections import deque

input = sys.stdin.readline
N = int(input()) # 보드의 선택
K = int(input()) # 사과의 개수
apple = [list(map(int, input().split())) for _ in range(K)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

L = int(input()) # 방향의 개수
direction = {} # 방향을 전환할 카운트와 방향
for _ in range(L):
    cnt, dist = input().split()
    direction[int(cnt)] = dist

print(snake_game())