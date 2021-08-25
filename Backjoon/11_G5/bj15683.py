# 15863. 감시

# 방법1. 개선 풀이(다른 사람 참고)
def see(x, y, d):  # cctv의 해당 방향의 좌표들을 반환
    res = set()
    for n in d:
        nx, ny = x + dx[n], y + dy[n]
        while (0<=nx<N) and (0<=ny<M) and room[nx][ny] != 6:  # 범위 내 / 벽이 아닐 때 반복
            if room[nx][ny] == 0:  # 감시할 수 있는 경우
                res.add((nx, ny))
            nx, ny = nx + dx[n], ny + dy[n]
    return res


def dfs(depth, arr):  # depth(cctv의 인덱스)가 최대가 됐을 때, 최소의 blank를 확인
    global result
    if depth == len(cctv):
        result = min(result, blank - len(arr))
        return

    for pos in cctv[depth]:  # 해당 cctv의 가능한 방향들을 반복
        dfs(depth+1, arr | pos)  # 원래의 좌표에서 가능한 좌표의 합집합을 구함(중복 좌표 안 생김)


import sys

input = sys.stdin.readline
N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)  # 이동 좌표
cctv = []  # 해당 cctv(인덱스)의 가능한 좌표들을 저장
result, blank = 64, 0  # 사각지대(문제 상 배열은 8*8), 초기 공백을 저장

for i in range(N*M):  # room 배열의 요소 수만큼 반복
    r, c = divmod(i, M)  # 행: 몫, 열: 나머지
    if room[r][c] == 0:  # 감시 가능한 공간인 경우
        blank += 1
    elif room[r][c] == 1:
        cctv.append( [see(r, c, [d]) for d in range(4)] )  # [0], [1], [2], [3]이 실행
    elif room[r][c] == 2:
        cctv.append( [see(r, c, [d, d + 2]) for d in range(2)] )  # [0, 2], [1, 3]이 실행
    elif room[r][c] == 3:
        cctv.append( [see(r, c, [d, (d+1) % 4]) for d in range(4)] )  # [0, 1], [1, 2], [2, 3], [3, 0]이 실행
    elif room[r][c] == 4:
        cctv.append( [see(r, c, [d, (d+1) % 4, (d+2) % 4]) for d in range(4)] ) # [0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]이 실행
    elif room[r][c] == 5:
        cctv.append( [see(r, c, [0, 1, 2, 3])] )  # [0, 1, 2, 3]이 실행

dfs(0, set())  # 시작 depth(인덱스) 0, 시작 집합
print(result)

# 방법2. 처음 풀이(pypy3 제출)
# def see(x, y, d, delta):
#     dx, dy, cnt = 0, 0, 0
#     if d == 0: dx = -1  # 상
#     elif d == 1: dy = 1  # 우
#     elif d == 2: dx = 1  # 하
#     else: dy = -1  # 좌

#     while True:
#         x += dx
#         y += dy
#         if (0<=x<N) and (0<=y<M) and room[x][y] != 6:
#             if 1<=room[x][y]<=5:
#                 continue
#             elif room[x][y] == 0:
#                 cnt += 1
#                 delta[x][y] = -1
#         else:
#             break


# def cctv(x, y, d, k, delta):
#     if k == 1:
#         if d == 0: return see(x, y, 0, delta)
#         elif d == 1: return see(x, y, 1, delta)
#         elif d == 2: return see(x, y, 2, delta)
#         else: return see(x, y, 3, delta)

#     elif k == 2:
#         if d == 0: see(x, y, 0, delta); see(x, y, 2, delta)
#         else: see(x, y, 1, delta); see(x, y, 3, delta)

#     elif k == 3:
#         if d == 0: see(x, y, 0, delta); see(x, y, 1, delta)
#         elif d == 1: see(x, y, 1, delta); see(x, y, 2, delta)
#         elif d == 2:  see(x, y, 2, delta); see(x, y, 3, delta)
#         else: see(x, y, 3, delta); see(x, y, 0, delta)

#     elif k == 4:
#         if d == 0: see(x, y, 0, delta); see(x, y, 1, delta); see(x, y, 2, delta)
#         elif d == 1: see(x, y, 1, delta); see(x, y, 2, delta); see(x, y, 3, delta)
#         elif d == 2: see(x, y, 2, delta); see(x, y, 3, delta); see(x, y, 0, delta)
#         else: see(x, y, 3, delta); see(x, y, 0, delta); see(x, y, 1, delta)

#     else: see(x, y, 0, delta); see(x, y, 1, delta); see(x, y, 2, delta); see(x, y, 3, delta)


# def check(arr):
#     result = 0
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 0:
#                 result += 1
#     return result

# def dfs(depth, arr):
#     global result, temp
#     if depth == len(cctv_coord):
#         result = min(result, check(arr))
#         return
    
#     temp = deepcopy(arr)
#     x, y, k = cctv_coord[depth]
#     for i in cctv_kind[k]:
#         cctv(x, y, i, k, temp)
#         dfs(depth+1, temp)
#         temp = deepcopy(arr)


# import sys
# from copy import deepcopy

# input = sys.stdin.readline
# N, M = map(int, input().split())
# room = [list(map(int, input().split())) for _ in range(N)]
# blank = len([i for i in range(N) for j in range(M) if room[i][j] == 0])
# cctv_coord = [(i, j, room[i][j]) for i in range(N) for j in range(M) if room[i][j] not in (0, 6)]
# cctv_kind = [[], [0, 1, 2, 3], [0, 1], [0, 1, 2, 3], [0, 1, 2, 3], [0]]
# result, temp = 64, 0
# dfs(0, room)
# print(result)
