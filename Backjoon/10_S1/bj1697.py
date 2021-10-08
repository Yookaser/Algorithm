# 1697. 숨바꼭질

# 방법1. DP
N, K = list(map(int, input().split()))

if N >= K:  # K가 작으면 -1씩 이동할 수 밖에 없음(같다면 0)
    print(N - K)
else:
    DP = list(reversed(range(0, N+1))) + [100001] * (K - N)
    
    for i in range(N+1, K+1):  # N부터 들어가면 line15에서 i-1 오류 발생할 수 있음(N=0일때)
        if i % 2 == 0:
            DP[i] = min(DP[i-1] + 1, DP[i//2] + 1)  # (바로 앞의 값 + 1 OR 2나눈 값 + 1) 중 작은 값
        else:
            DP[i] = min(DP[i-1] + 1, DP[(i+1)//2] + 2)  # (바로 앞의 값 + 1 OR 바로 뒤의 값을 2로 나눈 값 + 2) 중 작은 값
    print(DP[K])

# 방법2. BFS
from collections import deque


def bfs():
    if N >= K: return N - K

    q = deque([N])
    DP = [0] * 100001  # 초기값 0으로

    while q:
        x = q.popleft()
        
        if x == K:  # value가 찾는 값이랑 같은 경우
            return DP[K]
        
        for i in (x-1, x+1, x*2):  # 앞, 뒤, 2배
            if (-1<i<100001) and not DP[i]:  # DP 범위 내이고, 값 0인 경우
                DP[i] = DP[x] + 1  # i인덱스 갱신
                q += [i]


N, K = list(map(int, input().split()))
print(bfs())
