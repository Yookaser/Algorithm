# 14500. 테트로미노

# 방법1. 브루트 포스
def tetro_I(x, y): # I 모양 테트로미노
    total = tetro_map[x][y] # 초기값 저장
    tetromino = [[(1,0), (2,0), (3,0)], [(0,1), (0,2), (0,3)]] # 회전/대칭하면, 2가지 경우의 수

    for move in tetromino: # tetromino 리스트 요소 순회
        temp = tetro_map[x][y] # 해당 테트로미노의 합계를 구하기 위한 변수 // 초기값 저장
        for dx, dy in move: # 이동할 거리 반복
            if tetro_map[x+dx][y+dy] != -1: # 테두리가 아닌 경우(-1이면 테두리)
                temp += tetro_map[x+dx][y+dy] # 해당 좌표의 값 temp에 합함
            else: # 테두리인 경우
                break # 멈춤
        else: # 테두리에 안 걸린 경우
            total = max(total, temp) # total값과 비교하여 큰 값 선택

    return total

def tetro_O(x, y): # ㅁ 모양 테트로미노
    total = tetro_map[x][y]
    tetromino = [(1,0), (0,1), (1,1)] # 회전/대칭하면, 1가지 경우의 수

    for dx, dy in tetromino: # 이동할 거리 반복(다만, 여기서는 1번만 돌게 됨)
        if tetro_map[x+dx][y+dy] != -1:
            total += tetro_map[x+dx][y+dy] 
        else:
            break

    return total

def tetro_L(x, y): # L, J 모양 테트로미노(tetro_I와 같음 // 다시 문제를 풀 때는 반복을 함수화 시킬 필요가 있음)
    total = tetro_map[x][y]
    tetromino = [[(1,0), (2,0), (2,1)], [(1,0), (2,0), (2,-1)],
                 [(0,1), (0,2), (1,2)], [(0,1), (0,2), (-1,2)],
                 [(-1,0), (-2,0), (-2,1)], [(-1,0), (-2,0), (-2,-1)],
                 [(0,-1), (0,-2), (1,-2)], [(0,-1), (0,-2), (-1,-2)],
                 ] # 회전/대칭하면, 8가지 경우의 수(L, J 각각 4개씩)

    for move in tetromino:
        temp = tetro_map[x][y]
        for dx, dy in move:
            if tetro_map[x+dx][y+dy] != -1:
                temp += tetro_map[x+dx][y+dy] 
            else:
                break
        else:
            total = max(total, temp)

    return total

def tetro_Z(x, y): # Z, S 모양 테트로미노(tetro_I와 같음)
    total = tetro_map[x][y]
    tetromino = [[(0,1), (1,1), (1,2)], [(0,1), (-1,1), (-1,2)],
                 [(1,0), (1,1), (2,1)], [(1,0), (1,-1), (2,-1)]
                ] # 회전/대칭하면, 4가지 경우의 수

    for move in tetromino:
        temp = tetro_map[x][y]
        for dx, dy in move:
            if tetro_map[x+dx][y+dy] != -1:
                temp += tetro_map[x+dx][y+dy] 
            else:
                break
        else:
            total = max(total, temp)

    return total

def tetro_T(x, y): # T 모양 테트로미노(tetro_I와 같음)
    total = tetro_map[x][y]
    tetromino = [[(1,0), (2,0), (1,1)], [(0,-1), (0,-2), (1,-1)],
                 [(-1,0), (-2,0), (-1,-1)], [(0,1), (0,2), (-1,1)]
                ] # 회전/대칭하면, 4가지 경우의 수

    for move in tetromino:
        temp = tetro_map[x][y]
        for dx, dy in move:
            if tetro_map[x+dx][y+dy] != -1:
                temp += tetro_map[x+dx][y+dy] 
            else:
                break
        else:
            total = max(total, temp)

    return total

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
tetro_map = [[-1] * (M+2)] + [[] for i in range(N)] + [[-1] * (M+2)] # tetro_map 초기화(테두리는 -1 -> 자연수 1000까지 입력 받으므로)
result = 0 # 결과값 0으로 초기화(최소 0 이상이므로)

for i in range(1, N+1):
    tetro_map[i] = [-1] + list(map(int, input().split())) + [-1] # tetro_map 양식에 맞게 양 테두리 [-1] 포함해서 입력 받음

for x in range(1, N+1): # x, y를 반복함(범위 행: 1~N, 열: 1~M)
    for y in range(1, M+1):
        result = max(result, tetro_I(x, y), tetro_O(x, y), tetro_L(x, y), tetro_Z(x, y), tetro_T(x, y)) # 각 값의 최대값을 찾음

print(result)

# # 방법2. dfs
# def dfs(idx, x, y, value):
#     global result
#     if value + (4-idx) * maxi <= result: # 현재 상태가 tetro_map상 최대값을 남은 횟수만큼 더해도 result보다 작다면 조기 종료
#         return
#     if idx == 4: # 결과값에 도달한 경우
#         result = max(result, value) # 더 큰 값을 result에 저장
#         return # 추가 계산 방지를 위한 종료
#     for move in moves:
#         dx = x + move[0] # x좌표 이동
#         dy = y + move[1] # y좌표 이동
#         if tetro_map[dx][dy] != -1 and not visited[dx][dy]: # 테두리가 아니고, 방문한 적 없는 경우
#             visited[dx][dy] = True # 방문한 것으로 변경
#             if idx == 2: # 2인 경우(테트로미노가 T인 경우을 계산하기 위해)
#                 dfs(idx+1, x, y, value+tetro_map[dx][dy]) # 횟수 +1, value는 이동한 값을 더하고, 좌표는 해당 좌표로 다시 dfs 실행)
#             dfs(idx+1, dx, dy, value + tetro_map[dx][dy]) # 횟수 +1, value에 이동한 값을 더하고, 이동한 좌표로 다시 dfs 실행
#             visited[dx][dy] = False # dfs가 끝나고 나오면 실행되므로 해당 좌표 방문안 한 것으로 변경

# import sys

# input = sys.stdin.readline
# N, M = map(int, input().split())
# tetro_map = [[-1] * (M+2)] + [[] for i in range(N)] + [[-1] * (M+2)] # tetro_map 초기화(테두리는 -1 -> 자연수 1000까지 입력 받으므로)
# result = 0 # 결과값 0으로 초기화(최소 0 이상이므로)

# for i in range(1, N+1):
#     tetro_map[i] = [-1] + list(map(int, input().split())) + [-1] # tetro_map 양식에 맞게 양 테두리 [-1] 포함해서 입력 받음

# maxi = max(sum(tetro_map, [])) # 최대값 미리 저장(조기 종료를 위해서)
# moves = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우
# visited = [[False] * (M+2) for i in range(N+2)] # 방문했는지 여부를 저장할 공간

# for x in range(1, N+1): # x, y를 반복함(범위 행: 1~N, 열: 1~M)
#     for y in range(1, M+1):
#         visited[x][y] = True # 방문했다고 변경
#         dfs(1, x, y, tetro_map[x][y]) # 해당 좌표 dfs 진행
#         visited[x][y] = False # dfs 다 돌았으므로 방문안했다고 변경

# print(result)