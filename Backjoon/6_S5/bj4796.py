# 4796. 캠핑

from sys import stdin


input = stdin.readline
i = 0
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0: break  # 종료 조건
    i += 1
    a = V // P
    b = V % P

    if L<b: b = L
    print(f'Case {i}: {a * L + b}')
