# 2491. 수열

N = int(input())
arr = list(map(int, input().split()))
DP1, DP2 = [0] * N, [0] * N # DP1: 작아지지 않는 숫자, DP2: 커지지 않는 숫자
DP1[0], DP2[0] = 1, 1 # 초기값은 1(자기자신)

for i in range(1, N): # 범위 1~N
    if arr[i] > arr[i-1]: # 커진 경우
        DP1[i] = DP1[i-1] + 1
        DP2[i] = 1 # 커졌으므로 1로 초기화
    elif arr[i] < arr[i-1]:# 작아진 경우
        DP2[i] = DP2[i-1] + 1
        DP1[i] = 1 # 작아졌으므로 1로 초기화
    else: # 같은 경우(둘 다 증가)
        DP1[i] = DP1[i-1] + 1
        DP2[i] = DP2[i-1] + 1

print(max(max(DP1), max(DP2))) # 두 DP의 최대값에서 더 큰 값 출력