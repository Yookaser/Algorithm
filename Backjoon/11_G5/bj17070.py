# 17070. 파이프 옮기기 1

# 방법1. 다음에 이동할 곳에 + 하는 방식
import sys


input = sys.stdin.readline
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
DP = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]  # 가로, 대각선, 세로

DP[0][1][0] = 1  # 초기 위치

for x in range(N):
    for y in range(1, N):
        r, d, c = DP[x][y]  # 해당 좌표의 가로, 대각선, 세로 경우의 수
        if (x<N-1) and (y<N-1):
            if r:  # 가로 경우의 수가 있는 경우
                if A[x][y+1] == 0:
                    DP[x][y+1][0] += r  # 가로 이동
                    if A[x+1][y] == 0 and A[x+1][y+1] == 0:
                        DP[x+1][y+1][1] += r  # 대각선 이동

            if d:  # 대각선 경우의 수가 있는 경우
                if A[x][y+1] == 0:
                    DP[x][y+1][0] += d  # 가로 이동
                    if A[x+1][y] == 0 and A[x+1][y+1] == 0:
                        DP[x+1][y+1][1] += d  # 대각선 이동
                if A[x+1][y] == 0:
                    DP[x+1][y][2] += d  # 세로 이동

            if c:
                if A[x+1][y] == 0:
                    DP[x+1][y][2] += c  # 세로 이동
                    if A[x][y+1] == 0 and A[x+1][y+1] == 0:
                        DP[x+1][y+1][1] += c  # 대각선 이동
                
        elif x == N-1 and y < N-1:  # 맨 밑 좌표들
            if A[x][y+1] == 0:
                DP[x][y+1][0] += (r+d)  # 가로 + 대각선 이동
        elif y == N-1 and x < N-1:  # 맨 오른쪽 좌표들
            if A[x+1][y] == 0:
                DP[x+1][y][2] += (c+d)  # 세로 + 대각선 이동

print(sum(DP[N-1][N-1]))

# 방법2. 이동을 하고 + 하는 방식
# import sys


# input = sys.stdin.readline
# N = int(input())
# A = [list(map(int, input().split())) for _ in range(N)]
# DP = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]  # 가로, 대각선, 세로

# DP[0][1][0] = 1  # 초기 위치

# for i in range(2, N):  # 맨 위 좌표들 미리 채우기
#     if A[0][i]: break  # 한 번 벽이 나오면 멈춤
#     DP[0][i][0] = 1

# if A[1][1] == 0 and A[0][2] == 0 and A[1][2] == 0:  # 처음 좌표 대각선 이동 여부 고려(밑의 for문의 y를 2부터 주기 위해)
#     DP[1][2][1] = 1

# for x in range(1, N):
#     for y in range(2, N):
#         if A[x][y]: continue  # 현재 좌표가 벽인 경우 그냥 이동
#         DP[x][y][0] = DP[x][y-1][0] + DP[x][y-1][1]  # 현재 좌표의 가로의 경우의 수 = 왼쪽 좌표의 가로와 대각선 경우의 수
#         DP[x][y][2] = DP[x-1][y][1] + DP[x-1][y][2]  # 현재 좌표의 세로의 경우의 수 = 위 좌표의 세로와 대각선 경우의 수
#         if A[x-1][y] or A[x][y-1]: continue  # 위 or 왼쪽 좌표가 벽인 경우 넘어감(대각선을 구하기 위해)
#         DP[x][y][1] = sum(DP[x-1][y-1])  # 현재 좌표의 대각선 경우의 수 = 왼쪽 대각선 좌표의 모든 경우의 수

# print(sum(DP[N-1][N-1]))