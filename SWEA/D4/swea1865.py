# 1865. 동철이의 일 분배

# 방법1. DP(DFS, 비트마스크)
def dfs(idx, rec):  # 현재 위치, 방문 기록
    if rec == (1<<N) - 1: return 1  # 모든 곳을 방문한 경우 1 반환(곱셈이므로)
    if DP[idx][rec]: return DP[idx][rec]  # 이미 계산된 값이 있는 경우

    p = 0  # 최솟값 지정
    for i in range(N):
        if A[idx][i] and not (rec&(1<<i)):  # 값이 존재하고, 방문한 적 없는 경우
            p = max(p, A[idx][i]/100 * dfs(idx+1, rec|(1<<i)))  # 더 최대값을 저장(dfs는 idx+1시킴)
    DP[idx][rec] = p
    return p  # 최댓값 반환


ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    DP = [[0] * (1<<N) for _ in range(N)]  # DP(이진수를 10진수로 변환한 값을 인덱스로 지정하기 위함)
    ans.append('#{0} {1:.6f}'.format(tc, 100*dfs(0, 0)))
print(*ans, sep='\n')

# 방법2. DFS(느림)
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