# 2105. 디저트 카페

def dfs(idx, x, y, v, s):  # 방향, x좌표, y좌표, 디저트 종류(집합), 각 방향마다의 디저트 수 == 변의 길이(리스트)
    global res
    if idx == 2 and len(v) <= res//2: return  # 가지치기2
    if idx == 4:  # base case(모든 방향을 다 돈 경우)
        if x == r and y == c:  # 처음 위치인 경우
            res = max(res, len(v))
        return
     
    dx, dy = dxy[idx]
    nx, ny = x+dx, y+dy
    if (-1<nx<N) and (-1<ny<N):
        if A[nx][ny] not in v:
            v.add(A[nx][ny])
            s[idx] += 1
            dfs(idx, nx, ny, v, s)  # 백트래킹
            s[idx] -= 1
            v.remove(A[x+dx][ny])
    if s[idx]:  # 해당 방향에서 디저트를 얻은 경우
        dfs(idx+1, x, y, v, s)


ans = []
dxy = [(-1, -1), (-1, 1), (1, 1), (1, -1)]  # 좌상, 우상, 우하, 좌하
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for i in range(N*N):
        r, c = divmod(i, N)
        if r == 0 or c == (N-1): continue  # 가지치기1
        dfs(0, r, c, set(), [0, 0, 0, 0])
 
    res = -1 if res == 0 else res  # 갱신 안됐다면 -1로 지정
    ans.append('#{0} {1}'.format(tc, res))
 
print(*ans, sep='\n')
