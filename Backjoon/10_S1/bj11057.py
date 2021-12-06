# 11057. 오르막 수

N = int(input())

A = [1] * 10

for i in range(N-1):
    for j in range(1, 10):
        A[j] += A[j-1]

print(sum(A)%10007)
