# 1956. 운동(pypy3 제출)

from sys import stdin


input = stdin.readline
V, E = map(int, input().split())
INF = 10**7
DP = [[INF]*(V+1) for _ in range(V+1)]  # 최대로 초기화

for _ in range(E):  # 간선값 추가
    a, b, c = map(int, input().split())
    DP[a][b] = c

for k in range(1, V+1):  # 경유지
    for i in range(1, V+1):  # 출발지
        if i == k: continue  # 출발지와 경유지가 같으면 돌 필요 없음
        for j in range(1, V+1):  # 도착지
            if j == k: continue  # 도착지와 경유지가 같으면 돌 필요 없음(원래 노드로 돌아오는 것이 아니면 여기 i == j가 들어가야 함)
            if DP[i][j] > DP[i][k] + DP[k][j]:  # min보다 조건문 처리가 더 빨랐음(이유는 모르겠음)
                DP[i][j] = DP[i][k] + DP[k][j]

ans = INF
for i in range(1, V+1):  # 자기자신으로 돌아오는 노드 중 최소값 찾기
    ans = min(ans, DP[i][i])  # 조건문 처리보다 min이 더 빨랐음(이유는 모르겠음)

if ans == INF:
    print(-1)
else:
    print(ans)
