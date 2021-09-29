# 4803. 트리

from sys import stdin
from collections import deque
       

def bfs(n):
    q = deque([(n, 0)])  # 현재 노드, 이전 노드(첫 노드는 이전 노드가 없으므로 0으로)

    while q:
        n, m = q.popleft()

        for i in tree[n]:
            if i != m:  # 이전 노드가 아닌 경우(양방향이므로 처리해줘야 함)
                if i in v:  # 방문 기록이 있는 경우
                    return False
                q.append((i, n))  # 현재 노드, 이전 노드
                v.add(i)
    return True


input = stdin.readline
tc = 0
while 1:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    
    ans = 0
    v = set()
    tree = [set() for _ in range(N+1)]
    for _ in range(M):  # 양방향
        a, b = map(int, input().split())
        tree[a].add(b)
        tree[b].add(a)
    
    for i in range(1, N+1):
        if i not in v and bfs(i):  # 방문 기록이 없고, bfs 반환이 True인 경우
            ans += 1
    
    tc += 1
    if ans == 0:
        print(f'Case {tc}: No trees.')
    elif ans == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {ans} trees.')
