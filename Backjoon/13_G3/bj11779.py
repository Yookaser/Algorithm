# 11779. 최소비용 구하기2

def dijkstra(start):
    DP[start] = [0, [start]]  # 시작 코스트 0, 시작 경로 start로 지정
    bfs_list = []
    heappush(bfs_list, [0, start])  # 반드시 코스트를 앞에 오게 만들어서 최소 비용부터 탐색

    while bfs_list:
        c, n = heappop(bfs_list)

        if DP[n][0] < c:  # 현재 노드의 값이 이동한 비용보다 작은 경우(아래 갈 필요 X)
            continue

        if n == e:  # 답을 찾은 경우(최소비용을 먼저 탐색하므로 찾으면 바로 종료해도 됨)
            return DP[e]

        for n_n, n_c in arr[n].items():
            x = n_c + c  # 이동 비용 만들기
            if DP[n_n][0] > x:  # 이동한 비용이 더 작은 경우
                DP[n_n][0] = x  # 이동 비용 교체
                DP[n_n][1] = DP[n][1] + [n_n]  # 이동 경로를 추가
                heappush(bfs_list, [x, n_n])
    return DP[e]


import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N = int(input())
M = int(input())
arr = [{} for _ in range(N+1)]
INF = 10**9  # 문제 조건상 1,000(N) * 100,000(c)가 최대라고 생각함
DP = [[INF, []] for i in range(N+1)]  # [비용, 경로]로 사용(인덱스는 노드 값)

for _ in range(M):
    s, e, c = map(int, input().split())
    if e in arr[s]:  # 값이 이미 있는 경우
        arr[s][e] = min(arr[s][e], c)  # 더 최소값을 선택
    else:  # 값이 없는 경우
        arr[s][e] = c  # 딕셔너리 만들어줌

s, e = map(int, input().split())

result = dijkstra(s)

print(result[0])
print(len(result[1]))
print(*result[1])