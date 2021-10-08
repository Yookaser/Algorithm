# 12851. 숨바꼭질 2

from collections import deque


def bfs():
    if N >= K: return [N-K, 1]
    q = deque([N])
    DP = [[0, 0] for _ in range(100001)]  # [걸리는 시간, 갈 수 있는 경우의 수]
    DP[N][1] = 1  # 자기 자신은 1로 지정

    while q:
        x = q.popleft()
        
        if x == K:
            return DP[K]

        for i in (x-1, x+1, x*2):  # 앞, 뒤, 2배
            if (-1<i<100001):
                if DP[i][0] == 0:  # 값이 없는 경우(처음)
                    DP[i][0] = DP[x][0] + 1
                    DP[i][1] = DP[x][1]  # 처음인 경우 갈 수 있는 값은 전 노드의 값(Line5를 한 이유)
                    q.append(i)  # 처음인 경우만 q에 추가함
                elif DP[i][0] == DP[x][0] + 1:  # 처음이 아닌 경우는 원래 값과 같은지 물어봐야 함
                    DP[i][1] += DP[x][1]


N, K = map(int, input().split())

print(*bfs(), sep='\n')
