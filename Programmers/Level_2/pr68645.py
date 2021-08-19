# 68645. 삼각 달팽이

# 방법1

def solution(n):
    result = [[0] * i for i in range(1, n+1)]

    direc = 0 # 3으로 나눴을 때, 나머지에 따른 방향(0: 아래, 1: 오른쪽, 2: 대각선)
    state = 1 # 들어갈 값(1 ~ n(n+1))

    while direc < n: # 방향의 총 수는 n과 같음
        if direc % 3 == 0: # 아래인 경우
            for i in range(n-direc): # 횟수는 n부터 -1씩 줄어들게 됨(이를 n-direc으로 구현)
                result[i + 2*(direc//3)][direc//3] = state
                state += 1
        elif direc % 3 == 1: # 오른쪽인 경우
            for i in range(n-direc):
                result[n - 1 - direc//3][i + direc//3 + 1] = state
                state += 1
        else: # 대각선인 경우
            for i in range(n-direc):
                result[n - 2 - i - direc//3][n - 2 - i - 2*(direc//3)] = state
                state += 1

        direc += 1

    return sum(result, [])

# 방법2

# def solution(n):
#     result = [[0] * i for i in range(1, n+1)]

#     [row, col, cnt] = [-1, 0, 1] # 행, 열, 값 초기화

#     for i in range(n): # n까지
#         for j in range(n-i): # n-i까지(방향마다 하나씩 줄어듬)
#             if i % 3 == 0: # 아래인 경우
#                 row += 1 # 행 +1(그래서 초기값 -1)
            
#             elif i % 3 == 1: # 오른쪽인 경우
#                 col += 1 # 열 +1(처음 열 값은 1이어야 함. 그래서 초기값 0)
            
#             else: # 대각선인 경우
#                 row -= 1 # 행 -1
#                 col -= 1 # 열 -1
            
#             result[row][col] = cnt # 해당 행, 열에 값 입력
#             cnt += 1 # 값 +1

#     return sum(result, [])