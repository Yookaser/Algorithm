# 1976. 여행 가자

from sys import stdin


def find(x):  # 루트 노드를 찾는 함수
    if p[x] < 0: return x  # 음수인 경우 루트 노드
    p[x] = find(p[x])
    return p[x]


def union(x, y):  # 두 트리를 합치는 함수
    x, y = find(x), find(y)

    if x != y:  # 루트 노드가 같은 경우는 이미 같은 트리이므로 무시
        if p[x] > p[y]:  # 더 작은 트리를 합치기 위함(더 음수일수록 더 큰 트리임)
            p[y] += p[x]  # 루트 노드
            p[x] = y  # 합쳐지는 작은 트리
        else:
            p[x] += p[y]
            p[y] = x


input = stdin.readline
N = int(input())
M = int(input())
p = [-1] * (N)  # 초기는 모두 루트 노드로 설정(음수 => 루트)

for i in range(N):
    arr = list(input().split())
    for j in range(N):
        if arr[j] == '1':  # 연결된 경우 트리 합치기
            union(i, j)

arr = list(map(lambda x: int(x)-1, input().split()))  # 노드 - 1해서 입력받음

for i in range(1, len(arr)):
    if find(arr[i-1]) != find(arr[i]):  # 루트 노드가 다르면 갈 수 없음
        print('NO')
        break
else:
    print('YES')
