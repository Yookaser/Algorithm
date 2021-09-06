# 17837. 새로운 게임

def move(n):
    for i in range(K):
        x, y, d = c[i]
        nx, ny = x + dxy[d][0], y + dxy[d][1]
        e = C[x][y].index(i)  # C 맵에서 i번째 말의 시작 인덱스
        rev = False  # 좌표로 인한 방향 전환을 체크

        if not (-1<nx<N) or not (-1<ny<N):  # 좌표를 벗어난 경우(방향 전환, 다음 좌표 재정의)
            rev = True
            d = pair[d]
            c[i][2] = d
            nx, ny = x + dxy[d][0], y + dxy[d][1]

        if A[nx][ny] == 2:  # 파란색인 경우(좌표로 인한 방향 전환이 없었던 경우만 => 방향 전환, 다음 좌표 재정의)
            if not rev:
                d = pair[d]
                c[i][2] = d
                nx, ny = x + dxy[d][0], y + dxy[d][1]

        if (-1<nx<N) and (-1<ny<N) and A[nx][ny] != 2:  # 범위내이면서 파란색이 아닌 경우
            for j in C[x][y][e:]:  # 맵에서 좌표의 i 번째 말 위의 말들 전부 좌표 변환
                    c[j][0] = nx
                    c[j][1] = ny

            if A[nx][ny] == 0: C[nx][ny].extend(C[x][y][e:])  # 흰색인 경우(맵에서 다음 좌표에 그냥 추가)
            else: C[nx][ny].extend(C[x][y][e:][::-1])  # 빨간색인 경우(맵에서 다음 좌표에 역순으로 추가)
            
            C[x][y] = C[x][y][:e]  # 맵에서 원래 좌표에 제거

            if len(C[nx][ny]) >= 4:
                return True


def solve():
    for n in range(1, 1001):  # 반드시 1001까지 해야 함(1000번째도 있을 수 있음 // 또한, 처음부터 끝나는 경우는 없으므로 1부터 시작)
        if move(n):
            return n
    return -1


N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]  # 맵의 색상을 표시할 공간(0: 흰, 1: 빨, 2: 파)
C = [[[] for _ in range(N)] for _ in range(N)]  # 말들의 위치를 표시할 공간
c = []  # 좌표와 방향을 저장할 공간(순서대로 실행하기 위해)
dxy = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]  # 우좌상하
pair = {1:2, 2:1, 3:4, 4:3}  # 맞은편 매칭

for i in range(K):
    x, y, d = map(int, input().split())
    C[x-1][y-1] = [i]  # 인덱스만 저장
    c.append([x-1, y-1, d])  # 좌표와 방향을 저장

print(solve())
