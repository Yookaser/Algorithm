# 20040. 사이클 게임

from sys import stdin


def find(x):  # 루트 노드를 찾는 함수
    if p[x] < 0: return x  # 음수인 경우 루트 노드
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    x, y = find(x), find(y)

    if x != y:
        if p[x] <= p[y]:
            p[x] += p[y]
            p[y] = x
        else:
            p[y] += p[x]
            p[x] = y
    else:  # 같은 루트 노드를 가진 경우는 사이클이 생긴 것
        return True


input = stdin.readline
N, M = map(int, input().split())

p = [-1] * N
for i in range(1, M+1):
    a, b = map(int, input().split())
    
    if union(a, b):  # 사이클이 생긴 경우
        print(i)  # 바로 출력(백준 시스템 상 이후 값들 입력 안받아도 됨)
        break
else:  # 사이클이 끝까지 생기지 않은 경우
    print(0)
