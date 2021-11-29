# 11052. 카드 구매하기

N = int(input())
P = [0] + list(map(int, input().split()))

d = [0] * (N+1)
d[1] = P[1]
for i in range(2, N+1):
    for j in range(1, i+1):
        if d[i] < d[i-j] + P[j]:
            d[i] = d[i-j] + P[j]
print(d[N])
