# 11053. 가장 긴 증가하는 부분 수열

N = int(input())
arr = list(map(int, input().split()))
DP = [1] * N # 자기자신은 무조건 수열에 포함되므로 모두 1로 초기화

for i in range(N):
    for j in range(i): # 0~(i-1) 반복
        if arr[i] > arr[j] and DP[i] <= DP[j]: # i가 j보다 작은데 DP 값이 작거나 같은 경우
            DP[i] = DP[j] + 1 # DP의 해당 j값에서 +1

print(max(DP)) # 최대값 출력