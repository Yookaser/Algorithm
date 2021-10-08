# 1865. 동철이의 일 분배

# 방법1. DP(비트마스크)
ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    m = (1<<N)  # 전체 경우의 수
    DP = [1] + [0] * (m-1)
    for i in range(m):
        t = bin(i).count('1')  # 다음 인덱스를 찾는 코드
        for j in range(N):
            if not (i&(1<<j)):  # 겹치지 않는 경우
                DP[i|(1<<j)] = max(DP[i|(1<<j)], A[t][j]/100 * DP[i])  # 더 최댓값 저장
    
    ans.append('#{0} {1:.6f}'.format(tc, DP[-1]*100))
print(*ans, sep='\n')

# 방법2. DP(DFS, 비트마스크)
# def dfs(idx, rec):
#     if rec == END: return 1
#     if DP[rec]: return DP[rec]

#     p = 0
#     for i in range(N):
#         if not (rec&(1<<i)):
#             p = max(p, A[idx][i]/100 * dfs(idx+1, rec|(1<<i)))
#     DP[rec] = p
#     return p


# ans = []
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     A = [list(map(int, input().split())) for _ in range(N)]

#     END = (1<<N) - 1
#     DP = [0] * (END+1)
#     ans.append('#{0} {1:.6f}'.format(tc, 100*dfs(0, 0)))

# print(*ans, sep='\n')

# 방법3. DFS(느림)
# def dfs(idx, p):
#     global res
#     if p <= res: return  # 가지치기

#     if idx == N:  # base case
#         res = p
#         return

#     for i in range(N):
#         if v[i]:
#             v[i] = 0
#             dfs(idx+1, p*A[idx][i]/100)  # 백트래킹
#             v[i] = 1


# ans = []
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     A = [list(map(int, input().split())) for _ in range(N)]

#     res = 0
#     v = [1] * N  # 1은 방문 가능, 0은 방문 불가의 의미
#     dfs(0, 1)
#     ans.append('#{0} {1:.6f}'.format(tc, 100*res))

# print(*ans, sep='\n')