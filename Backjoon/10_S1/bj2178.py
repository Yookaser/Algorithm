# 2178. 미로 탐색

def bfs(cnt):
    visited_list = deque([(1, 1)]) # 제일 처음 방문하는 지역

    while visited_list:
        x, y = visited_list.popleft() # x, y값 받기(현재 위치를 의미)

        if x == N and y == M: # 해당 지점에 도달한 경우
            return maze[x][y] # 미로의 값 반환(미로의 값이 1인 경우 변경할 것임)

        for (x_g, y_g) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]: # 위, 아래, 왼쪽, 오른쪽
            if maze[x_g][y_g] != 0 and maze[x_g][y_g] == 1: # 0이 아니고(갈 수 없는 곳), 1인 곳(2 이상의 값은 이미 변경한 곳)
                maze[x_g][y_g] = maze[x][y] + 1 # bfs이므로 가장 근처부터 방문함 따라서 현재 위치에서 이동할 위치는 +1로 계산 
                visited_list.append((x_g, y_g)) # 방문했던 or 앞으로 방문할 지역에 추가

from collections import deque            
import sys

input = sys.stdin.readline # input은 문제 없으나, sys.stdin.readline은 입력받을 때, '/n'이 붙으니 주의! [:-1]하면 /n 한번에 떼어짐(즉, 하나의 문자로 생각)

N, M = list(map(int, input().split()))
maze = [[0] * (M+2)] + [[] for i in range(N)] + [[0] * (M+2)] # 주변 테두리를 0으로 채운 미로를 만들기 위해(이러면 범위로 인한 문제가 줄어듬)

for i in range(1, N+1):
    maze[i] = [0] + list(map(int, list(input()[:-1]))) +  [0] # 주변 테두리를 0으로 채운 미로를 만들기 위해(이러면 범위로 인한 문제가 줄어듬)

print(bfs(0))