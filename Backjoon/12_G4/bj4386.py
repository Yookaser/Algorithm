# 4386. 별자리 만들기

from sys import stdin


def dist(x, y):  # 두 점의 거리 구하는 함수
    return round(((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5, 2)


def find(x):  # 루트 노드를 찾는 함수
    if p[x] < 0: return x  # 음수인 경우 루트 노드
    p[x] = find(p[x])
    return p[x]


def union(x, y):  # 두 트리를 합치는 함수
    x, y = find(x), find(y)

    if x != y:  # 루트 노드가 다른 경우
        if p[x] <= p[y]:
            p[x] += p[y]
            p[y] = x
        else:
            p[y] += p[x]
            p[x] = y
        return True
    return False


input = stdin.readline
N = int(input())
A = [tuple(map(float, input().split())) for _ in range(N)]

grp = []
for i in range(N):
    for j in range(i+1, N):
        grp.append((i, j, dist(A[i], A[j])))


p = [-1] * (N+1)
grp.sort(key=lambda x: x[2])  # 거리 기준으로 정렬

ans = cnt = 0  # 최종 결과, 계산된 간선의 개수
for a, b, c in grp:
    if union(a, b):  # 루트 노드가 다른 경우(즉 사이클이 아닌 경우)
        cnt += 1
        ans += c
        if cnt == N-1: break  # V-1개의 간선을 확인하면 종료

print(ans)
