# 16235. 나무 재테크

# 다른 사람의 좋은 풀이를 구현함
from collections import defaultdict


def spring_summer():  # 봄, 여름은 한 번에 처리
    for r in range(N):
        for c in range(N):
            nu = 0  # 해당 칸의 추가될 양분(죽은 나무로 인한)
            temp = defaultdict(int)  # 해당 좌표 새로운 나무 딕셔너리를 저장
            for a, t in sorted(T[r][c].items()):  # 해당 좌표에 나무 나이, 나무 수 반복
                live = min(arr[r][c]//a, t)  # 살아 있는 나무의 수 계산
                die = t - live
                if live > 0:  # 살아있는 나무가 있는 경우
                    arr[r][c] -= a * live  # 나무가 먹을 양분 뻬기
                    temp[a+1] += live  # 나이 +1
                nu += (a//2) * die  # 양분의 (나무의 나이 // 2) * (죽은 나무의 수)
            
            T[r][c] = temp  # 나무 딕셔너리 갱신
            arr[r][c] += nu  # 죽은 나무의 양분을 추가


def fall():
    for r in range(N):
        for c in range(N):
            for a, t in T[r][c].items():  # 해당 좌표에 나무 나이, 나무 수 반복
                if a % 5 == 0 and t != 0:
                    for dr, dc in move:
                        nr, nc = r + dr, c + dc
                        if (-1<nr<N) and (-1<nc<N):
                            T[nr][nc][1] += t  # 나이가 1인 나무 번식


def winter():
    for r in range(N):
        for c in range(N):
            arr[r][c] += A[r][c]


N, M, K = map(int, input().split())
arr = [[5] * N for _ in range(N)]  # 초기 양분
move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # 이동(8칸)
A = [list(map(int, input().split())) * N for _ in range(N)]  # 추가 양분
T = [[defaultdict(int) for _ in range(N)] for _ in range(N)]  # 나무 맵(각 칸에 딕셔너리로 저장(기본값 0) // 반드시 내부도 for문으로 만들기 곱하기 안됨)

for _ in range(M):
    x, y, z = map(int, input().split())
    T[x-1][y-1][z] += 1  # 해당 좌표에 딕셔러니 값으로 추가(키: 나이, 값: 나무 수)

for _ in range(K):  # 계절 반복
    spring_summer()
    fall()
    winter()

ans = 0
for r in range(N):
    for c in range(N):
        for t in T[r][c].values():  # 각 좌표마다 T의 값을 더함
            ans += t

print(ans)
