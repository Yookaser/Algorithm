# 2019. 더블더블

N = int(input())

arr = list(range(N + 1))
solu = list(map(lambda x: 2**x, arr))
print(*solu)