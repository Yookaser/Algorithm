# 1005. ACM Craft

import sys
from collections import defaultdict


def dfs(n):
    if dp[n] != -1: return dp[n]  # 이미 갱신된 경우(갱신된 값 반환)

    if not grp[n]: dp[n] = time[n-1]  # 리프 노드인 경우(해당 time값을 저장)
    else:
        m = 0
        for nn in grp[n]:  # 다이나믹 프로그래밍 적용부분
            m = max(dfs(nn), m)
        dp[n] = time[n-1] + m  # 해당 노드로 오는 최대값과 해당 노드의 건설 시간을 더함
    return dp[n]


ans = []
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = tuple(map(int, input().split()))

    grp = defaultdict(list)
    for _ in range(K):
        X, Y = map(int, input().split())
        grp[Y].append(X)  # W부터 시작해야하므로 반대로 입력
    
    W = int(input())

    dp = [-1] * (N+1)  # 해당 노드까지 오는데 최대 비용을 저장할 dp
    ans.append(dfs(W))  # W부터 시작
print(*ans, sep='\n')
