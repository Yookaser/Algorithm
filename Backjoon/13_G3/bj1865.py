# 1865. 웜홀

from sys import stdin


def go(s):
    DP = [INF] * (N+1)  # 다익스트라처럼 모든 노드 가장 최대값
    DP[s] = 0  # 시작값만 0으로

    for _ in range(N):  # N번 반복
        flag = False
        for n in range(1, N+1):  # 1~N노드 순회
            for nn, d in grp[n]:  # 각 노드에서 (이동할 노드, 시간(거리))를 반복
                if DP[nn] > DP[n] + d:  # 다음 노드의 시간이 (현재 노드+이동 시간)보다 큰 경우
                    DP[nn] = DP[n] + d  # 갱신
                    flag = True
        if not flag:  # 갱신이 일어나지 않은 경우(음수 사이클이 있으면 계속 갱신됨)
            break
    return flag


input = stdin.readline
T = int(input())
INF = 5 * (1e7)  # 문제상 최대값은 2,500(도로의 수) * 10,000(시간의 최대값)이라고 생각함
for _ in range(T):
    N, M, W = map(int, input().split())
    grp = [[] for _ in range(N+1)]

    for i in range(M):  # 도로는 양방향이므로 꼭 반대로도 넣어줘야 함
        S, E, T = map(int, input().split())
        grp[S].append((E, T))
        grp[E].append((S, T))
    
    for i in range(W):  # 웜홀은 단방향이므로 반대로 넣으면 안됨
        S, E, T = map(int, input().split())
        grp[S].append((E, -T))

    if go(1):
        print('YES')
    else:
        print('NO')
