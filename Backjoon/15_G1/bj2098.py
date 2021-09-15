# 2098. 외판원 순회

from sys import stdin


def dfs(cur, rec):  # 현재 위치, 방문 기록
    if rec == (1<<N) - 1:  # 모든 곳을 방문한 경우
        return W[cur][0] or INF  # 0번이 시작이자 끝임
    if DP[cur][rec]:  # 이미 계산된 값이 있는 경우
        return DP[cur][rec]  # 해당 값 반환
    
    d = INF
    for i in range(N):
        if not W[cur][i] or rec&(1<<i):  # 갈 수 없거나 방문한 경우 PASS
            continue
        d = min(d, W[cur][i] + dfs(i, rec|(1<<i)))  # d 갱신
    DP[cur][rec] = d
    return d  # d 반환


input = stdin.readline
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * (1<<N) for _ in range(N)]  # DP(이진수를 10진수로 변환한 값을 인덱스로 지정하기 위함)
INF = 10**7  # 문제상 최대값은 16 * (10**6)

print(dfs(0, 1))  # 0번부터 시작(방문을 표시하기 위해 두 번째 매개변수를 1로 놓음)
