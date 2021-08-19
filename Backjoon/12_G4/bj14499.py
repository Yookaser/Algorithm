# 14499. 주사위 굴리기

def diceRoll(x, y):
    for i in K:
        if 0 <= x + move[i][0] < N and 0 <= y + move[i][1] < M: # 맵 안에서 이동하는 경우
            x += move[i][0]
            y += move[i][1]
            
            # 문제의 전개도에서 1을 윗면으로 놓고 돌려볼 것(6은 밑면)
            if i == 1: # 동쪽 roll
                dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
            elif i == 2: # 서쪽 roll
                dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
            elif i == 3: # 북쪽 roll
                dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
            else: # 남쪽 roll
                dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

            if dice_map[x][y] == 0: # 지도가 0인 경우
                dice_map[x][y] = dice[6] # 문제 조건
            else: # 0이 아닌 경우
                dice[6] = dice_map[x][y] # 값을 받음
                dice_map[x][y] = 0 # 지도를 0으로 변경
            print(dice[1]) # 윗면 출력


N, M, x, y, K = map(int, input().split())
dice_map = [list(map(int, input().split())) for _ in range(N)]
K = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0, 0] # 주사위(숫자와 인덱스를 맞춤)
move = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)] # 이동(방향 입력과 인덱스를 맞춤)

diceRoll(x, y)