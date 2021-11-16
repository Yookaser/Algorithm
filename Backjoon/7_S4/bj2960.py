# 2960. 에라토스네스의 체

def solve():
    cnt = 0
    A = [1] * (N+1)

    for i in range(2, len(A)+1):
        for j in range(i, N+1, i):
            if A[j]:
                A[j] = 0
                cnt += 1
                if cnt == K:  # 종료조건 체크
                    return j


N, K = map(int, input().split()) 
print(solve())
