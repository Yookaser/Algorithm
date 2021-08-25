# 15684. 사다리 조작

def play():
    for col in range(1, N+1):  # 열 반복
        state = col
        for row in range(1, H+1):  # 계속 타고 내려가면서 변경 
            state += ladder[row][state]
        if state != col:  # 전부 타고 내려왔는데, 기존 열과 다른 경우 중지
            return False
    return True


def dfs(cnt, idx):
    global result
    if play():  # 정답인 경우
        result = min(result, cnt)  # 더 최솟값 선택
        return
    if cnt+1 >= result:  # **핵심**(+1을 해줘서 비교해야 함 => 그래야 밑에 반복문 안 돌음)
        return

    for cur in range(idx, len(coords)):  # 가능한 좌표의 인덱스 반복
        r, c = coords[cur]  # 가로, 세로
        if not ladder[r][c] and not ladder[r][c+1]:  # 자기 자신과 오른쪽을 수정 가능한 경우
            ladder[r][c], ladder[r][c+1] = 1, -1  # 수정
            dfs(cnt+1, cur)  # 재귀
            ladder[r][c], ladder[r][c+1] = 0, 0 # 원상복귀


import sys

input = sys.stdin.readline
N, M, H = map(int, input().split())
ladder = [[0] * (N+1) for _ in range(H+1)]
coords = [(i, j) for i in range(1, H+1) for j in range(1, N) if not ladder[i][j] and not ladder[i][j+1]]  # 가능한 좌표

for i in range(M):  # 이동 사다리 표시
    a, b = map(int, input().split())
    ladder[a][b] = 1  # 좌측 +1
    ladder[a][b+1] = -1  # 우측 -1

result = 4  # 최대 3이므로 4로 지정
dfs(0, 0)  # 횟수, idx
print(result) if result != 4 else print(-1)  # result가 갱신 안됐으면 -1 출력
