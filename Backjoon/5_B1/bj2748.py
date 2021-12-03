# 2748. 피보나치 수 2

N = int(input())
A = [0, 1]

for i in range(N-1):  # N-1번 반복
    A.append(A[-2]+A[-1])

print(A[-1])
