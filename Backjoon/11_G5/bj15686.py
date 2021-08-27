# 15686. 치킨 배달

import sys


def street(arr1):  # 조합된 인덱스와 거리를 계산하는 함수
    res = 0
    for i in range(len(s1)):  # 집의 인덱스 반복
        m = 100
        for j in arr1:  # 조합된 치킨집 인덱스 반복
            m = min(m, DP[i][j])  # 최솟값 찾기
        res += m  # 최솟값 더하기
    return res


def dfs(depth, idx, arr):  # 치킨집 인덱스 조합(M개)
    global sol
    if depth == M:
        sol = min(sol, street(arr))
    else:
        for i in range(idx, len(s2)):
            arr.append(i)  # 인덱스를 더해줌
            dfs(depth+1, i+1, arr)
            arr.pop()


input = sys.stdin.readline
N, M = map(int, input().split())
ar = [list(map(int, input().split())) for _ in range(N)]

s1, s2 = [], []  # 집, 치킨집 좌표를 저장할 리스트
for i in range(N**2):  # 집과 치킨집 좌표 찾기
    r, c = divmod(i, N)
    if ar[r][c] == 1:
        s1.append((r, c))
    elif ar[r][c] == 2:
        s2.append((r, c))

DP = [[0] * len(s2) for _ in range((len(s1)))]  # 집과 치킨집의 거리를 저장할 리스트
for i in range(len(s1)):
        for j in range(len(s2)):
            DP[i][j] = abs(s1[i][0]-s2[j][0])+abs(s1[i][1]-s2[j][1])  # 거리를 저장(i는 집의 인덱스 순서, j는 치킨집의 인덱스 순서)

sol = 10000
dfs(0, 0, [])
print(sol)
