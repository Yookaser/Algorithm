# 13549. 숨바꼭질 3

N, K = map(int, input().split())

if N >= K: 
    print(N-K) # 2배수로 접근 안되므로 그냥 출력
else:
    DP = list(range(N+1))[::-1] + [100001] * (K-N) # N보다 작으면 무조건 -1로만 접근 가능함

    for i in range(N+1, K+1):
        if i % 2: # 홀수인 경우
            DP[i] = min(DP[i-1]+1, DP[(i+1)//2]+1)
        else: # 짝수인 경우
            DP[i] = min(DP[i-1]+1, DP[i//2])
        
    print(DP[K])