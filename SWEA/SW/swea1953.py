# 1953. 탈주범 검거

from collections import deque


def bfs(x, y):  # 반드시 bfs 사용할 것(dfs 구현 힘듬)
    q = deque([(x, y, 1)])
    v = set([(R, C)])

    while q:
        x, y, t = q.popleft()
        
        if t == L:  # 종료 조건
            continue
    
        for i in dic1[arr[x][y]]:
            nx, ny = x + xy[i][0], y + xy[i][1]
            if (nx, ny) not in v and (-1<nx<N) and (-1<ny<M):  # 방문한 적 없고 범위 내인 경우
                if arr[nx][ny] in dic2[i]:  # 이동 가능한 경우(연결된 파이프여야 함)
                    v.add((nx, ny))
                    q.append((nx, ny, t+1))
    return len(v)


ans = []
xy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dic1 = {1: [0,1,2,3], 2: [0,2], 3: [1,3], 4: [0,1], 5: [1,2], 6: [2,3], 7: [0,3]}  # 파이프(key)에 따른 이동 가능한 방향 리스트(상우하좌)
dic2 = {0: (1, 2, 5, 6), 1: (1, 3, 6, 7), 2: (1, 2, 4, 7), 3: (1, 3, 4, 5)}  # 방향(key)에 따른 연결 파이프 리스트(상우하좌)
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    ans.append('#{0} {1}'.format(tc, bfs(R, C)))

print(*ans, sep='\n')
