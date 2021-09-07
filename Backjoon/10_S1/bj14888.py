# 14888. 연산자 끼워넣기

import sys


def calculation(now, i, a, s, m, d):
    global maxvalue, minvalue
    if i == N:
        maxvalue = max(maxvalue, now)
        minvalue = min(minvalue, now)
        return
    else:
        if a: calculation(now+num_list[i], i+1, a-1, s, m, d)  # +
        if s: calculation(now-num_list[i], i+1, a, s-1, m, d)  # -
        if m: calculation(now*num_list[i], i+1, a, s, m-1, d)  # *
        if d: calculation(int(now/num_list[i]), i+1, a, s, m, d-1)  # /(단, 정수로 변환해야 함)


N = int(input())
num_list = list(map(int, input().split()))
c1, c2, c3, c4 = map(int, input().split())
maxvalue = -sys.maxsize
minvalue = sys.maxsize

calculation(num_list[0], 1, c1, c2, c3, c4)

print(maxvalue)
print(minvalue)
