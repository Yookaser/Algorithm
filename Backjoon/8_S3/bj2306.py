# 2306. 바이러스

def bfs(num):
    bfs_list = [num] # 해당 bfs를 통해 순회한 노드들이 들어갈 공간
    visited_list = deque([num]) # 순회를 위해 방문했던 노드를 잠시 저장할 공간

    while visited_list:
        value = visited_list.popleft() # 어떤 노드와 연결된 가장 작은 수부터 돌게 만듬(leftpop)
        for i in range(1, N + 1): # 범위는 주의해야 함(1~N으로 설정해야 함)
            if network[value][i] == 1 and i not in bfs_list: # value 노드와 연결되어 있고, 방문한 적 없는 경우
                visited_list.append(i)
                bfs_list.append(i)

    return len(bfs_list) - 1 # bfs_list의 길이를 반환하는데 이때, 1은 제외해야 하므로 -1

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
network = [[0] * (N+1) for i in range(N+1)] # 인덱스 오류를 피하기 위해 0행, 0열도 생성

for _ in range(M):
    x, y = list(map(int, input().split()))
    network[x][y] = network[y][x] = 1 # 양방향이므로 둘 다 1로 바꿔줘야 함

print(bfs(1)) # 컴퓨터1로 감염되는 컴퓨터만 구하면 되므로 1을 넣음