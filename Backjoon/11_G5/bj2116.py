# 2116. 주사위 쌓기

def dice_stack(idx, value, face):
    global result # 값을 변경해야 하므로 dfs 선언
    if idx == len(arr): # 주사위 다 쌓은 경우
        result = max(result, value) # 최대값 비교
        return

    next_face = arr[idx][facing[arr[idx].index(face)]] # 밑면과 마주보는 면(윗 면)
    rest = max(set(arr[idx]) - set([face, next_face])) # 밑면, 윗면을 제외한 최대값(여기서 시간이 많이 걸리는 것 같음)
    dice_stack(idx+1, value + rest , next_face) # 재귀

import sys

sys.setrecursionlimit(10**6)
N = int(input())
result = 0
facing = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0} # 맞은편을 가리키는 인덱스
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(6): # 밑면을 무엇으로 둘 것인지?
    next_face = facing[i] # 밑면과 마주보는 면(윗 면)
    rest = max(set(arr[0]) - set([arr[0][i], arr[0][next_face]])) # 밑면, 윗면을 제외한 최대값(여기서 시간이 많이 걸리는 것 같음)
    dice_stack(1, rest, arr[0][next_face]) # 깊이, 현재값, 윗면

print(result)