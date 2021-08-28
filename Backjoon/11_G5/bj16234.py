# 16234. 인구 이동

# 매 회차(날)마다 모든 좌표를 돌게되면 느려짐
# 처음만 모든 좌표를 돌고, 이후에는 필요한 좌표만 돌아야 됨
# 이는 bfs 내부에서 인구이동이 일어날 때, 해당 좌표를 go에 추가해줌으로써 구현
# 이때, 밖의 while에서 go의 길이만큼 반복하게 만들어서 for문 내부에서 길이가 달라지는 상황을 막아야 함
# 이를 고려해서 append, pop을 왼쪽에서 할지 오른쪽에서 할지 고려해야 함
import sys
from collections import deque


def bfs(x, y, ans):
    q = deque([(x, y)])
    v = [(x, y)]
    p = arr[x][y]  # 초기 인구는 입력받은 좌표로
    tv[x][y] = ans  # 해당 좌표의 방문 표시

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (-1<nx<N) and (-1<ny<N):  # 범위 내인지 확인
                if tv[nx][ny] != ans and (L<=abs(arr[x][y]-arr[nx][ny])<=R):  # 이번 회차에 방문 안했고, 조건 인구 차이 내인지 확인
                    q.append((nx, ny))
                    v.append((nx, ny))
                    tv[nx][ny] = ans  # 방문 표시
                    p += arr[nx][ny]  # 해당 좌표 인구 더하기
    
    if len(v) > 1:  # 길이가 1 이상인 경우(초기에 1개 좌표를 입력해둠)
        avg = p // len(v)  # 평균 구하기
        for r, c in v:
            arr[r][c] = avg  # 해당 좌표 인구를 평균으로
            go.appendleft((r, c))  # 로직상 반드시 왼쪽에서 더해야 함
        return True  # 인구 이동이 있었음을 반환
    else:
        return False  # 인구 이동이 없었음을 반환


input = sys.stdin.readline
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

go = deque([(i, j) for i in range(N) for j in range(N)])  # 방문할 좌표 만들기

ans = 0  # 인구 이동한 날짜
while True:
    tv = [[-1] * N for _ in range(N)]  # 방문 표시할 좌표(ans로 계속 갱신됐는지로 확인)
    flag = True  # flag가 for문을 돌고도 True면 멈출 것임

    for i in range(len(go)):  # 반드시 현재의 go의 길이만큼만!(for 내부에서 계속 변화함)
        r, c = go.pop()  # 뒤에서 pop(bfs 내부에서 왼쪽에서 append하기 때문)
        if tv[r][c] != ans:  # 현재 날짜로 갱신이 됐는지
            if bfs(r, c, ans):  # bfs가 True를 반환하면(인구 이동이 일어나면)
                flag = False  # flag를 False로 바꿔서 멈추지 않게 만듬
                
    if flag:  # 정지 조건
        break
    ans += 1  # 날짜 +1

print(ans)
