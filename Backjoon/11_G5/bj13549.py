# 13549. 숨바꼭질 3

# 방법1. DP
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

# 방법2. BFS
# def bfs():  # 역순으로 접근
#     if N >= K: return N - K
#     q = [K]
#     DP = [0] * 100001
#     DP[K] = 1  # DP의 값이 0인지에 따라 방문 체크를 해야하므로 1로 변환(답 출력 때 -1)

#     while q:
#         q2 = []
        
#         for i in q:
#             if i == N:
#                 return DP[N] - 1  # 출력 시 -1
#             if not (i%2) and i >= N:  # 짝수이고, N보다 클 때(N보다 작은 수에서 접근할 수 있음)
#                 DP[i//2] = DP[i]
#                 q.append(i//2)
#             q2.append(i)

#         q = []  # 초기화 해줘야 함
#         for i in q2:
#             for j in (i-1, i+1):  # 앞, 뒤
#                 if (-1<j<100001) and not DP[j]:
#                     DP[j] = DP[i] + 1
#                     q.append(j)
    

# N, K = map(int, input().split())

# print(bfs())
