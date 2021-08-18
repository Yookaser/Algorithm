# 12100. 2048 (Easy)

# 방법1. 내 풀이(느림..)

def moveLeft(arr): # 왼쪽으로 이동하는 함수
    arr2 = deepcopy(arr) # 깊은 복사
    confirm = [[True]*N for _ in range(N)] # 합쳐질 수 있는지 나타내는 리스트(False 못 합쳐짐)
    for row in range(0, N): # 왼쪽으로 움직일 수 있는 가장 가까운 것부터 반복
        for col in range(1, N):
            if arr2[row][col] != 0: # 값이 있는 경우
                value = arr2[row][col]
                arr2[row][col] = 0 # 이동해야 하므로 일단 0으로 변환
                while (col-1) >= 0 and arr2[row][col-1] == 0: # 이동 좌표가 범위 내, 0인 경우 반복
                    col -= 1
                if (col-1) >= 0 and arr2[row][col-1] == value and confirm[row][col-1]: # 이동 좌표가 범위 내, 같은 값, 합쳐진 적 없는 경우
                    arr2[row][col-1] = value * 2
                    confirm[row][col-1] = False # 합쳐진 것으로 변경
                else: # 같은 값이 아닌 경우
                    arr2[row][col] = value
    return arr2

def moveRight(arr): # 오른쪽으로 이동하는 함수
    arr2 = deepcopy(arr)
    confirm = [[True]*N for _ in range(N)]
    for row in range(0, N):
        for col in range(N-2, -1, -1):
            if arr2[row][col] != 0:
                value = arr2[row][col]
                arr2[row][col] = 0
                while (col+1) <= (N-1) and arr2[row][col+1] == 0:
                    col += 1
                if (col+1) <= (N-1) and arr2[row][col+1] == value and confirm[row][col+1]:
                    arr2[row][col+1] = value * 2
                    confirm[row][col+1] = False
                else:
                    arr2[row][col] = value
    return arr2

def moveUp(arr): # 위쪽으로 이동하는 함수
    result = moveLeft(list(map(list, zip(*arr)))) # 행과 열을 뒤집어서 moveLeft 실행
    return list(map(list, zip(*result))) # 다시 뒤집어서 반환

def moveDown(arr): # 아래쪽으로 이동하는 함수
    result = moveRight(list(map(list, zip(*arr))))
    return list(map(list, zip(*result)))


def dfs(arr, depth):
    global result
    if depth == 5: # 5회 반복한 경우
        result = max(result, max(sum(arr, []))) # 기존 결과값과 리스트의 최대값 중 큰 값을 저장
        return

    arr2 = moveLeft(arr)
    if arr2 != arr: dfs(arr2, depth+1) # 왼쪽 이동 것이 기존 리스트와 다른 경우 이동
    
    arr2 = moveRight(arr)
    if arr2 != arr: dfs(arr2, depth+1) # 오른쪽 이동 것이 기존 리스트와 다른 경우 이동

    arr2 = moveUp(arr)
    if arr2 != arr: dfs(arr2, depth+1) # 위쪽 이동 것이 기존 리스트와 다른 경우 이동

    arr2 = moveDown(arr)
    if arr2 != arr: dfs(arr2, depth+1) # 아래쪽 이동한 것이 기존 리스트와 다른 경우 이동

    result = max(result, max(sum(arr, []))) # 만약, 모두 이동이 불가능한 경우를 대비하기 위해 필요함(밑의 테스트 케이스 확인)
    return


import sys
from copy import deepcopy

input = sys.stdin.readline
N = int(input())
result = 0
arr = [list(map(int, input().split())) for _ in range(N)]

dfs(arr, 0)
print(result)


# 방법2. 다른 풀이 참고(빠름..)

def moveX(arr, dist='L'): # 왼쪽 오른쪽으로 이동(dist가 왼쪽인지 오른쪽인지 결정)
    result = []
    for row in arr:
        if dist == 'R': # 오른쪽인 경우(뒤집음)
            row.reverse()
        temp_row = []
        value = 0
        for factor in row:
            if factor != 0: # 0이 아닌 경우(0이면 고려할 필요 없음)
                if value == factor: # 값과 요소가 같은 경우
                    temp_row[-1] *= 2
                    value = 0
                else: # 값이 다른 경우
                    temp_row.append(factor) # 그냥 추가
                    value = factor # value 값을 저장함
        temp_row += [0] * (N - len(temp_row)) # 숫자를 다 채운 후 뒤는 0으로 채움
        if dist == 'R': # 오른쪽인 경우(뒤집음)
            temp_row.reverse()
        result.append(temp_row) # 결과에 한 행씩 추가
    return result

def moveY(arr, dist='U'): # 위쪽 아래쪽으로 이동(dist가 위쪽인지 아래쪽인지 결정)
    if dist == 'U': # 위쪽인 경우
        result = moveX(list(map(list, zip(*arr))), 'L') # 행과 열을 뒤집음(이때 moveX의 왼쪽으로 해야 함)
        return list(map(list, zip(*result))) # 다시 행과 열을 뒤집음
    else: # 아래쪽인 경우
        result = moveX(list(map(list, zip(*arr))), 'R')
        return list(map(list, zip(*result)))


def dfs(arr, depth):
    global result
    if depth == 5:
        result = max(result, max(sum(arr, [])))
        return
    else:
        arr2 = moveX(arr, 'L')
        if arr2 != arr: dfs(arr2, depth+1) # 왼쪽 이동 것이 기존 리스트와 다른 경우 이동
        
        arr2 = moveX(arr, 'R')
        if arr2 != arr: dfs(arr2, depth+1) # 오른쪽 이동 것이 기존 리스트와 다른 경우 이동

        arr2 = moveY(arr, 'U')
        if arr2 != arr: dfs(arr2, depth+1) # 위쪽 이동 것이 기존 리스트와 다른 경우 이동

        arr2 = moveY(arr, 'D')
        if arr2 != arr: dfs(arr2, depth+1) # 아래쪽 이동한 것이 기존 리스트와 다른 경우 이동

        result = max(result, max(sum(arr, []))) # 만약, 모두 이동이 불가능한 경우를 대비하기 위해 필요함(밑의 테스트 케이스 확인)
        return


import sys

input = sys.stdin.readline
N = int(input())
result = 0
arr = [list(map(int, input().split())) for _ in range(N)]

dfs(arr, 0)
print(result)

'''
4
2 4 8 16
4 8 16 32
8 16 32 64
16 32 64 128
'''