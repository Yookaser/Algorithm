# 9251. LCS

A, B = input(), input()

DP = [''] * len(B)  # B가 열의 역할을 하게 됨

for i in range(len(A)):
    t = 0  # 이전 i에서 최대값을 가져오는 역할
    for j in range(len(B)):
        if t < DP[j]: t = DP[j]  # 최대값을 가져오기
        elif A[i] == B[j]: DP[j] = t + 1  # 같으면 + 1

print(max(DP))