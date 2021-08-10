# 11725. 트리의 부모 찾기

def bfs(start):
    confirm = set([start]) # 방문했는지 여부를 체크할 집합
    visited = deque([start]) # 방문 기록을 임시 저장할 공간

    while visited:
        node = visited.popleft()
        for i in tree[node]:
            if i not in confirm:
                result[i] = node # 결과 저장(node가 부모임)
                confirm.add(i)
                visited.append(i)


import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)] # 연결된 노드를 저장할 공간
result = [0] * (N+1) # 인덱스: 자식 노드 // 인덱스값: 부모 노드

while 1: # 입력 받기(종료 조건이 명시 안되어 있음)
    try:
        parent, child = map(int, input().split())
        tree[parent].append(child) # 무엇이 부모인지 자식인지 알 수 없으므로
        tree[child].append(parent) # 둘 다 추가함
    except: # 더 이상 입력이 없는 경우
        break

bfs(1) # 루트가 1이므로 아래로 진행
print(*result[2:], sep='\n') # 2번째 노드부터 출력임