# 6603. 로또

def dfs(n, d):
    if d == 6:  # base case
        for i in range(6):
            print(A[i], end=' ')
        print()
        return
    
    for i in range(n, len(S)):
        A[d] = S[i]
        dfs(i+1, d+1)


A = [0] * 13  # 원소의 길이 ==> 7 ~ 12

while True:
    S = list(map(int, input().split()))

    if not S[0]: break
    dfs(1, 0)  # S의 첫 번째수는 무시
    print()
