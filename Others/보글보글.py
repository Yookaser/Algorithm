# 보글보글 (https://algospot.com/judge/problem/read/BOGGLE)

def boglebogle(idx, dx, dy):
    global confirm # 값을 변경해야 하므로 global 선언(False -> True)
    if idx == len(word) or confirm: # 찾는 단어 길이와 idx가 같거나 이미 답을 찾은 경우
        confirm = True # True로 변경
        return # 추가적인 계산을 막기 위한 return(반환의 의미는 아님 -> 여기서 반환해도 for문 안에 있는 경우가 있으므로 의미 X)

    for x, y in xy: # 이동 반복
        if bogle_map[dx + x][dy + y] == word[idx] and (dx+x, dy+y, idx) not in visited: # 해당 좌표 값이 찾는 글자이고, 방문하지 않은 경우
            visited.add((dx + x, dy + y, idx)) # 방문 기록을 남김(idx가 없으면 해당 좌표 다시 방문 못함 -> 반드시 idx가 같은 경우 같은 좌표를 방문 못하게 해야 함)
            boglebogle(idx+1, dx + x, dy + y) # 재귀(idx는 +1)

import sys

input = sys.stdin.readline
C = int(input())
xy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)] # x, y가 움직일 공간(12시부터 시계 방향)

for i in range(C):
    bogle_map = [[0] * 7] + [[] for _ in range(5)] + [[0] * 7] # 테두리 0으로 만들어줌
    
    for i in range(1, 6): # 테두리가 있으므로 범위 주의
        bogle_map[i] = [0] + list(input().rstrip()) + [0] # 입력받는 값 양 끝에 0을 더해서 테두리 만듬

    N = int(input())

    for _ in range(N):
        confirm = False # 답을 찾았을 때, 불필요한 재귀들을 더 이상 안 돌게 하기 위한 변수(값 찾으면 True로 바꿈)
        word = input().rstrip() # sys.stdin.readline은 입력값 뒤에 '\n' 붙으므로 rstrip()으로 제거
        visited = set() # 방문했는지 점검하기 위한 집합(단, (x좌표, y좌표, idx)의 특이한 값을 사용// 단순 확인이므로 집합 사용)

        start_list = [(i, j) for i in range(7) for j in range(7) if bogle_map[i][j] == word[0]] # 첫 단어와 일치하는 좌표 확인(여기서도 범위는 5가 아닌 7)
        for i, j in start_list: # 해당 좌표 반복
            boglebogle(1, i, j) # 재귀 시작(입력할 때, idx(몇 번째 글자인지 확인할 변수)는 1로 함 -> 이미 첫 단어 찾았으므로)
            if confirm: # 답을 찾은 경우
                print(word, 'YES')
                break
        else: # 못 찾은 경우(for문이 정상적으로 반복 후)
            print(word, 'NO')