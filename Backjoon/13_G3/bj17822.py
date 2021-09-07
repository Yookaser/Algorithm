# 17822. 원판 돌리기

import sys


def rotation(x, d, k):
    I = [0] * (N)  # I: 시작 인덱스
    res = [[] for _ in range(N)]  # res: 회전된 원판

    if d == 0: k *= -1  # 시계방향이면 -k

    for i in range(x, N+1, x):  # x의 배수가 모두 변해야 함
        I[i-1] = (I[i-1] + k) % M

    for x in range(N):  # 회전 적용
        res[x] = A[x][I[x]:]
        res[x].extend(A[x][:I[x]])

    return res
        

def delete():
    global c, v
    s = set()  # s: 상하좌우 하나라도 같은 좌표

    for i in range(N*M):
        x, y = divmod(i, M)
        if A[x][y] != 0:  # 0은 제외함
            for dx, dy in D:
                nx, ny = x+dx, (y+dy) % M  # x는 위 아래가 연결된 것이 아니므로 나머지 계산 안함
                if (-1<nx<N) and A[x][y] == A[nx][ny] and (nx, ny) not in s:  # x가 범위 내이고, 상하좌우 중 하나라도 같고, 이동 좌표를 방문한 적 없을 때
                    s.update([(x, y), (nx, ny)])  # 죄표 추가
    
    if s:  # 하나라도 같은 좌표가 있는 경우
        for x, y in s:
            c -= 1  # 개수 -
            v -= A[x][y]  # 합계 -
            A[x][y] = 0  # 0으로 갱신
    elif c != 0:  # 같은 좌표가 없고, 0이 아닌 숫자의 개수가 0이 아닌 경우
        a = v / c  # 평균(int로 구하면 안됨)
        for i in range(N*M):
            x, y = divmod(i, M)
            if A[x][y] != 0:
                if A[x][y] > a:
                    A[x][y] -= 1
                    v -= 1  # 합계 -1
                elif A[x][y] < a:
                    A[x][y] += 1
                    v += 1  # 합계 +1


input = sys.stdin.readline
N, M, T = map(int, input().split())
D = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # D: 이동방향(상하좌우)
A = [list(map(int, input().split())) for _ in range(N)]  # A: 원판

c, v = N*M, sum(sum(A, []))  # c: 개수, v: 합계
for _ in range(T):
    x, d, k = map(int, input().split())
    A = rotation(x, d, k)
    delete()

print(sum(sum(A, [])))
