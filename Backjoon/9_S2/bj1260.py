# 1260. DFS와 BFS

def DFS(start): # 시작값만 받기
    global DFS_result # 함수 내에서 전역에 선언된 리스트 요인 변경 가능해서 전역 선언 안해도 되는 줄 알았으나, 오류 발생하므로 전역 변수 선언
    DFS_result += [start] # 들어온 값 결과 리스트에 더하기

    if len(DFS_result) >= len(point_map) - 1: # Base Case(딱히, 선언 안 해줘도 되지만, 조금이라도 시간 단축 가능할 것 같아서 만듬)
        return

    for i in range(1, len(point_map)): # 1~N 반복(0은 불필요)
        if point_map[start][i] == 1 and i not in DFS_result: # 간선이 있고, 해당 값을 방문한 적 없는 경우
            DFS(i) # 재귀

def BFS(start):
    global BFS_result
    BFS_result = [start] # 초기값 더하기(BFS는 재귀가 아니므로 초기값만 설정하면 됨)
    visit_list = [start] # 방문했었고, 앞으로 해당 값으로 반복하기 위한 리스트

    while visit_list: # visit_list가 0이면 끝남
        value = visit_list.pop(0) # 제일 처음 값의 노드 저장
        for i in range(len(point_map)): # 해당 노드를 반복
            if point_map[value][i] == 1 and i not in BFS_result: # 간선이 있고, 해당 값을 방문한 적 없는 경우
                BFS_result += [i] # 들어온 값 결과 리스트에 더하기
                visit_list += [i] # 방문 리스트에도 더하기(앞으로 반복할 값들)

import sys

input = sys.stdin.readline

N, M, V = list(map(int, input().split()))
point_map = [[0] * (N + 1) for i in range(N + 1)] # 인덱스 헷갈리지 않기 위해 0~N(N + 1개)로 만듬
DFS_result = [] # DFS 결과 저장할 리스트(함수 내에서 프린트하는 로직이면 필요 없음)
BFS_result = [] # BFS 결과 저장할 리스트(함수 내에서 프린트하는 로직이면 필요 없음)

for i in range(M):
    x, y = list(map(int, input().split()))
    point_map[x][y] = 1
    point_map[y][x] = 1 # 양방향이므로 반대도 해줘야 함

DFS(V)
BFS(V)
print(*DFS_result)
print(*BFS_result)