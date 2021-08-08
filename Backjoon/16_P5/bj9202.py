# 9202. Boggle

# 방법1. DFS(pypy3)
def boglebogle(x, y, idx):
    global confirm # False -> True로 값 변경해야 하므로 global

    if idx == len(word) or confirm: # 단어 길이와 같아졌거나 답을 이미 찾은 경우
        confirm = True
        return

    visited.add((x, y)) # 방문한 곳 다시 방문 X(문제 조건)
    for dx, dy in xy:
        if board_map[x+dx][y+dy] == word[idx] and (x+dx, y+dy) not in visited:
            boglebogle(x+dx, y+dy, idx+1)
    visited.remove((x, y)) # 해당 dfs가 끝나면 해당 좌표를 다른 dfs가 다시 방문할 수 있도록 해줘야 함

def getPoint(length): # 점수 변환 함수
    if len(word) >= 8:
        return 11
    elif len(word) >= 7:
        return 5
    elif len(word) >= 6:
        return 3
    elif len(word) >= 5:
        return 2
    elif len(word) >= 3:
        return 1
    else:
        return 0

import sys

input = sys.stdin.readline
W = int(input())
words = []

for _ in range(W):
    words.append(input().rstrip()) # sys.stdin.readline로 input할 땐, '\n' 지워줘야 함

input() # 입력의 공백 채우기

B = int(input())
xy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)] # x, y가 움직일 공간(12시부터 시계 방향)

for board in range(B):
    board_map = [[0] * 6] + [[] for _ in range(4)] + [[0] * 6] # 테두리 0으로 만들어줌
    
    for i in range(1, 5):
        board_map[i] = [0] + list(input().rstrip()) + [0] # 입력받는 값 양 끝에 0을 더해서 테두리 만듬
    
    if board != B - 1: # 입력의 공백 채우기
        input()

    max_length = -1 # word의 길이 비교를 위한 변수
    point = 0 # 각 board마다의 총 점수
    long_word = '' # 가장 긴 단어
    find_word = 0 # 찾은 단어의 개수
    
    for word in words: # 단어 반복
        confirm = False # 해당 단어를 찾았는지 여부를 나타내는 변수
        for m in range(1, 5):
            if confirm: # 단어를 찾았으면 더 돌 필요 X(문제 조건)
                break
            for n in range(1, 5):
                if board_map[m][n] == word[0]: # 시작 단어의 좌표를 찾은 경우
                    visited = set() # 방문 여부를 나타냄
                    boglebogle(m, n, 1) # x, y, 깊이(단어 1개는 이미 찾았으므로 1)
                
                    if confirm: # 답을 찾은 경우
                        find_word += 1
                        point += getPoint(len(word)) # 점수는 getPoint함수 이용

                        if max_length < len(word): # 현재 단어가 지금까지 단어의 최고 길이보다 긴 경우
                            max_length = len(word)
                            long_word = word
                        elif max_length == len(word): # 현재 단어와 지금까지 단어의 최고 길이와 같은 경우
                            long_word = word if long_word > word else long_word # 사전상 더 빠른 단어로 long_word 교체

                        break # 답을 찾았으므로 더 이상 돌 필요 X(안쪽 for문 종료)
        
    print(point, long_word, find_word)

# 방법2. 트리, DFS(아직 구현 못하겠음 참고 => https://gist.github.com/sujin-lee0909/5dc8a8c3ba3da173cdf71bc72bb62f50)