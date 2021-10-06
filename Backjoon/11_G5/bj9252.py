# 9252. LCS 2

A, B = input(), input()

DP = [''] * len(B)  # B가 열의 역할을 하게 됨

for i in range(len(A)):
    t = ''  # 이전 i에서 최대값을 가져오는 역할
    for j in range(len(B)):
        if len(t) < len(DP[j]): t = DP[j]    # 최대값을 가져오기
        elif A[i] == B[j]: DP[j] = t + A[i]    # 같으면 + 1

res = ''
for w in DP:  # 가장 긴 값을 가져오기 위한 반복문
    if len(w) > len(res):
        res = w

print(len(res), res, sep='\n')
