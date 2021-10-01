# 1767. 프로세서 연결하기

def go(x, y, dx, dy, v):  # 이동 좌표를 구하는 함수
    t = set()
    nx, ny = x + dx, y+dy
    while (-1<nx<N) and (-1<ny<N):  # 범위 내인 경우를 반복
        if (nx, ny) in v:  # 벗어난 경우 빈 집합 반환
            return set()
        t.add((nx, ny))
        nx += dx
        ny += dy
    return t


def dfs(c, i, v):
    global res, m
    if (len(core)-i) + c < m:  # 가지치기1 => core 개수를 기준으로
        return
    if (len(core)-i) + c == m and len(v) - C >= res:  # 가지치기2 => 전선 개수를 기준으로
        return

    if i == len(core):  # base case
        if c > m:  # 큰 경우
            m = c
            res = len(v) - C
        elif c == m:  # 같은 경우
            res = min(res, len(v)-C)
        return

    for j in range(4):  # 상하좌우
        if not wire[i][j] or v & wire[i][j]: continue  # 이동 못하거나 전선 겹치는 경우
        dfs(c+1, i+1, v | wire[i][j])  # 전선을 놓을 수 있는 상황
    dfs(c, i+1, v)  # 전선을 놓을 수 없는 상황


ans = []
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = set((i, j) for i in range(N) for j in range(N) if arr[i][j] == 1)
    C = len(v)  # 전체 Core 개수

    core = []
    for r in range(1, N-1):  # 가장자리를 제외한 코어 리스트 생성
        for c in range(1, N-1):
            if arr[r][c]:
                core.append((r, c))

    wire = [{} for _ in range(len(core))]  # 상하좌우에 따라 가능한 좌표 저장
    for i in range(len(core)):
        for j, xy in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]):
            wire[i][j] = go(core[i][0], core[i][1], xy[0], xy[1], v)  # i => 코어 번호, j => 상하좌우(0|1|2|3)

    m, res = 0, N**2  # m => core, ans => 전선
    dfs(0, 0, v)  # 전력 연결된 코어, 인덱스, 방문 기록
    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')
