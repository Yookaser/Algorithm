# 1958. LCS 3

A, B, C = ' ' + input(), ' ' + input(), ' ' + input()  # 인덱스 처리를 위해 공백 미리 설정

DP = [[[0] * (len(C)) for _ in range(len(B))] for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        for k in range(1, len(C)):
            if A[i] == B[j] == C[k]:
                DP[i][j][k] = DP[i-1][j-1][k-1] + 1  # 직전의 값에서 +1
            else:
                DP[i][j][k] = max(DP[i-1][j][k], DP[i][j-1][k], DP[i][j][k-1])  # 3개의 경우 중 최대값

print(DP[-1][-1][-1])
