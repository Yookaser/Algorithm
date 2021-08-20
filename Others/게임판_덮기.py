# 게임판 덮기 (https://algospot.com/judge/problem/read/BOARDCOVER)

# 방법1. 성공한 코드

def findpoint():  # 첫 시작지점을 찾는 함수
    for i in range(H):
        for j in range(W):
            if board[i][j] == '.':
                return i, j
    return -1, -1  # 블럭을 다 채운 경우

def ispossible(x, y, L):  # 블럭이 들어갈 수 있는지 점검하는 함수
    for dx, dy in move[L]:
        nx = x + dx
        ny = y + dy
        if not (0<=nx<H and 0<=ny<W):  # 범위 이외
            return False
        if board[nx][ny] == '#':  # 블럭이 들어갈 수 없음
            return False
    return True  # 블럭이 들어갈 수 있는 경우

def change(x, y, L, delta):  # 값을 바꾸는 함수
    for dx, dy in move[L]:
        nx = x + dx
        ny = y + dy
        board[nx][ny] = delta  # 지정한 값으로 변환

def boardcover():
    x, y = findpoint()
    
    if x == -1 and y == -1:  # 블럭을 다 채운 경우
        return 1
    
    result = 0  # 시작값 0
    for L in range(4):  # 방향 순환
        if ispossible(x, y, L):  # 가능한 경우
            change(x, y, L, '#')  # 블럭 채우기
            result += boardcover()
            change(x, y, L, '.')  # 블럭 치우기
    return result


move = [[(0,0),(1,0),(0,1)], [(0,0),(1,0),(1,1)], [(0,0),(1,0),(1,-1)], [(0,0),(0,1),(1,1)]]  # 왼쪽 맨위부터 실행하므로 4가지임(16가지가 아님)
C = int(input())
for _ in range(C):
    H, W = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(H)]

    print(boardcover())

# 방법2. 실패한 코드

# def boardcover(idx, board):
#     global result
#     if len(board) == len(blank):
#         result += 1
#         return

#     for i in range(idx, len(blank)):
#         x, y = blank[i][0], blank[i][1]
#         if (x, y) not in board:
#             for L in move:
#                 temp = {(x, y)}
#                 for dx, dy in L:
#                     nx, ny = x + dx, y + dy
#                     if (nx, ny) in blank and (nx,ny) not in board:
#                         temp.add((nx, ny))
#                     else:
#                         break
#                 else:
#                     board.update(temp)
#                     boardcover(0, board)
#                     board = board.difference(temp)

# move = [[(1,0),(0,1)], [(1,0),(1,1)], [(1,0),(1,-1)], [(0,1),(1,1)]]
# C = int(input())
# for _ in range(C):
#     H, W = map(int, input().split())
#     game_map = [list(input().rstrip()) for _ in range(H)]
#     result = 0

#     blank = [(i, j) for i in range(H) for j in range(W) if game_map[i][j] == '.']
#     boardcover(0, set())
#     print(result)