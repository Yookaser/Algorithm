# 2467. 용액

N = int(input())
A = tuple(map(int, input().split()))

s, e = 0, N - 1
ans = [abs(A[s]+A[e]), A[s], A[e]]  # 최소값, 시작 값, 끝 값
while s < e:
    if ans[0] > abs(A[e]+A[s]):  # 갱신할지 확인
        ans = [abs(A[e]+A[s]), A[s], A[e]]
        
    if A[e] + A[s] > 0: e -= 1
    else: s += 1

print(ans[1], ans[2])
