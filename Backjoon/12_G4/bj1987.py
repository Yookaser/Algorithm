# 1987. 알파벳

from sys import stdin


input = stdin.readline
R, C = map(int, input().split())
A = [tuple(input()) for _ in range(R)]
V = [['']*C for _ in range(R)]  # 메모이제이션을 위한 리스트

ans = 0
q = [(0, 0, 1, A[0][0])]
while q:  # dfs 진행
    x, y, c, v = q.pop()  # x좌표, y좌표, 카운팅, 방문기록(문자열)
    if ans < c:
        ans = c
        if ans == 26: break  # 최대인 경우
    
    for nx, ny in ((x-1, y), (x, y+1), (x+1, y), (x, y-1)):
        if not (-1<nx<R) or not (-1<ny<C) or A[nx][ny] in v: continue
        t = v + A[nx][ny]
        if V[nx][ny] != t:  # 다른 경우 == 갱신된 경우(따라서 이 경우만 q에 추가)
            V[nx][ny] = t
            q.append((nx, ny, c+1, t))

print(ans)
