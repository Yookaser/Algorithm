N = int(input())
arr = list(map(int, input().split()))
DP1 = [1] * N # 증가하는 수열(자기자신은 무조건 수열에 포함되므로 모두 1로 초기화)
DP2 = [1] * N # 감소하는 수열(자기자신은 무조건 수열에 포함되므로 모두 1로 초기화)
DP = [0] * N # 증가하는 수열과 감소하는 수열의 합을 구할 리스트

for i in range(N):
    for j in range(i): # 0~(i-1) 반복
        if arr[i] > arr[j] and DP1[i] <= DP1[j]: # i가 j보다 작은데 DP 값이 작거나 같은 경우
            DP1[i] = DP1[j] + 1

for i in reversed(range(N)):
    for j in range(i+1, N): # (i+1)~(N-1) 반복
        if arr[i] > arr[j] and DP2[i] <= DP2[j]: # i가 j보다 작은데 DP 값이 작거나 같은 경우
            DP2[i] = DP2[j] + 1

for i in range(N): # 증가하는 수열과 감소하는 수열의 합 DP에 저장
    DP[i] = DP1[i] + DP2[i]

print(max(DP)-1) # 초기값을 1로 선언해줬으므로 자기자신이 중복되어 더해져 있으므로 -1