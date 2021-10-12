# 4195. 친구 네트워크

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
    
    return max(-p[x], -p[y])  # 둘 중 큰 값을 반환(해당 숫자가 집합의 크기)


ans = []
input = stdin.readline
T = int(input())
for _ in range(T):
    try:  # input이 안들어오는 경우도 생각해야 함
        F = int(input())

        p = [-1] * 200001  # t가 1부터 시작하므로 반드시 200001로 해야 함

        t = 1  # p의 인덱스 값을 가리킴
        friend = {}
        for _ in range(F):
            a, b = input().split()
            if a not in friend:
                friend[a] = t
                t += 1
            if b not in friend:
                friend[b] = t
                t += 1

            ans.append(union(friend[a], friend[b]))  # 결과 저장
    except:
        ans.append('')  # 안들어오면 공백 출력

print(*ans, sep='\n')
