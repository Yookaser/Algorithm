# 1032. 명령 프롬프트

from sys import stdin


input = stdin.readline
N = int(input())
A = list(input())

for i in range(N-1):
    B = list(input())
    for j in range(len(A)):
        if A[j] != B[j]:
            A[j] = '?'
            
print(''.join(A))