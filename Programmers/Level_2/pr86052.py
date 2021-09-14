# 86052. 빛의 경로 사이클

def solution(grid):
    R, C = len(grid), len(grid[0])
    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌
    grf = [[[0,0,0,0] for _ in range(C)] for _ in range(R)]  # 상우하좌
    
    
    def solve(x, y, d):
        res = 0
        while not grf[x][y][d]:  # 해당 좌표가 0이 아닐때까지 반복
            grf[x][y][d] = 1
            x, y = (x+dxy[d][0]) % R, (y+dxy[d][1]) % C  # x, y 이동
            if grid[x][y] == 'L': d = (d+1) % 4  # 좌회전
            elif grid[x][y] == 'R': d = (d-1) % 4  # 우회전
            res += 1  # 카운트
        return res
    
    
    ans = []
    for i in range(R):  # 행 반복
        for j in range(C):  # 열 반복
            for k in range(4):  # 노드의 방향 반복
                if grf[i][j][k] == 0:  # 0인 경우(방문 X인 경우)
                    ans.append(solve(i, j, k))             
    return sorted(ans)
