# 1311. 할 일 정하기 1

# 방법1. DFS & DP
from sys import stdin


def dfs(cur, rec):  # 현재 위치, 방문 기록
    if cur == N:  # 모든 일이 정해진 경우
        return 0
    if DP[cur][rec]:  # 이미 계산된 값이 있는 경우
        return DP[cur][rec]
    
    w = 10**6  # 문제상 최대값은 20 * (10**5)
    for i in range(N):
        if rec & (1<<i):  # 방문한 경우 PASS
            continue
        w = min(w, D[cur][i] + dfs(cur+1, rec|(1<<i)))  # d 갱신
    DP[cur][rec] = w
    return w


input = stdin.readline
N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * (1<<N) for _ in range(N)]  # DP(이진수를 10진수로 변환한 값을 인덱스로 지정하기 위함)

print(dfs(0, 0))

# 방법2. DP(더 빠름)
# from sys import stdin


# input = stdin.readline
# N = int(input())
# D = [list(map(int, input().split())) for _ in range(N)]
# DP = [[0] * (1<<N) for _ in range(N)]  # DP(이진수를 10진수로 변환한 값을 인덱스로 지정하기 위함)

# for i in range(N):  # 0번 사람의 일을 미리 정해두기
#     DP[0][1<<i] = D[0][i]

# for i in range(1, N):
#     for j in range(1<<N):  # (1<<N) 길이만큼 체크(range(N)이면 안됨 -> 비트의 각 자리수끼리 더해질 수도 있으므로)
#         if DP[i-1][j] != 0:
#             for k in range(N):
#                 if j&(1<<k):  # 방문한 적 있으면 PASS
#                     continue
#                 DP[i][j|(1<<k)] = (DP[i-1][j]+D[i][k]) if DP[i][j|(1<<k)] == 0 else min(DP[i][j|(1<<k)], DP[i-1][j] + D[i][k])  # DP 초기값이 0이므로 이를 고려

# print(DP[N-1][(1<<N)-1])
