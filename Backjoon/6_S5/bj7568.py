# 7568. 덩치

N = int(input())
people_size = [[] for _ in range(N)] # 사이즈 리스트 초기화
result = [0] * N # 등수 결과 리스트 초기화

for n in range(N): # 사이즈 입력 받기
    people_size[n] = list(map(int, input().split()))

for i in range(N):
    cnt = 1 # 등수는 1등부터 시작
    for j in range(N):
        if people_size[i][0] < people_size[j][0] and people_size[i][1] < people_size[j][1]: # 키, 몸무게 모두 작은 경우
            cnt += 1 # 등수 +1
    result[i] = cnt # 등수 결과 저장

print(*result)