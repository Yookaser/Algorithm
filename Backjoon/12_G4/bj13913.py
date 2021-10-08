# 13913. 숨바꼭질 4

def bfs():
    if N >= K:
        print(N-K)
        return [i for i in range(N, K-1, -1)]

    q = [N]
    DP = [-1 for _ in range(100001)]  # 해당 인덱스로 온 인덱스를 가리킬 것
    DP[N] = 0  # 출발지는 0으로

    while q:
        q2 = []

        for i in q:
            if i == K: break
            for j in (i-1, i+1, i*2):  # 앞, 뒤, 2배
                if not (-1<j<100001): continue  # 범위 밖이면 PASS
                if DP[j] == -1:
                    DP[j] = i  # 자신으로 온 인덱스를 가리킴
                    q2.append(j)
        
        q = q2[:]  # q 갱신

    res, k = [K], K  # 경로, k(K값 변경을 위해)
    while k != N:  # 시작 지점으로 돌아올 때까지
        res.append(DP[k])  # 역순으로 추가
        k = DP[k]

    print(len(res)-1)
    return res[::-1]


N, K = map(int, input().split())
print(*bfs())
