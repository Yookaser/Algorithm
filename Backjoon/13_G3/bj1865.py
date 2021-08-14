# 1865. 웜홀

def bf(start):
    DP = [INF] * (N+1) # 다익스트라처럼 모든 노드 가장 최대값
    DP[start] = 0 # 시작값만 0으로

    for i in range(N): # N번 돌려서 (N-1)번째 노드가 갱신되는지 확인하는 것
        for node in range(1, N+1): # 1~N노드 순회
            for next_node, dist in node_map[node]: # 각 노드에서 (이동할 노드, 시간(거리))를 반복
                if DP[next_node] > DP[node] + dist: # 다음 노드의 시간이 (현재 노드+이동 시간)보다 큰 경우
                    DP[next_node] = DP[node] + dist # 갱신
                    if i == (N-1): # N-1번째 갱신이 일어나는 경우(음수 사이클이 존재한다는 것)
                        return True
    return False

T = int(input())
INF = 5 * (1e7) # 문제상 최대값은 2,500(도로의 수) * 10,000(시간의 최대값)이라고 생각함
for _ in range(T):
    N, M, W = map(int, input().split())
    node_map = [[] for _ in range(N+1)]

    for i in range(M): # 도로는 양방향이므로 꼭 반대로도 넣어줘야 함
        S, E, T = map(int, input().split())
        node_map[S].append((E, T))
        node_map[E].append((S, T))
    
    for i in range(W): # 웜홀은 단방향이므로 반대로 넣으면 안됨
        S, E, T = map(int, input().split())
        node_map[S].append((E, -T))

    if bf(1):
        print('YES')
    else:
        print('NO')