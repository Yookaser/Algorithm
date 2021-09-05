# 2441. 별 찍기 - 4

N = int(input())
for i in reversed(range(1, N+1)):
    print(' ' * (N-i), '*' * (i), sep='')