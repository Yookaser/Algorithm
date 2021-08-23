# 14503. 로봇 청소기

def vacuum(x, y, d):
    global cnt
    if room[x][y] == 0:  # 해당 좌표를 청소할 수 있는 경우
        room[x][y] = -1  # 청소로 표시
        cnt += 1

    for _ in range(4):  # 방향을 반복
        d = (d-1) % 4  # 왼쪽 방향으로
        if room[x+move[d][0]][y+move[d][1]] == 0:  # 한 칸 이동했을 때, 청소할 수 있는 경우
            vacuum(x+move[d][0], y+move[d][1], d)  # 이동
            break
    else:  # for문을 정상적으로 끝낸 경우(방향을 4번 돌았으므로 다시 원래 방향)
        if room[x-move[d][0]][y-move[d][1]] == 1:  # 후진했을 때, 벽인 경우
            return
        vacuum(x-move[d][0], y-move[d][1], d)  # 후진


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
move = [(-1,0), (0, 1), (1,0), (0,-1)]
cnt = 0

vacuum(r, c, d)
print(cnt)
