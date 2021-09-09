# 11047. 동전 0

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
count = 0
    
arr.sort(reverse = True)  # 역순으로 정렬(큰 값부터 계산해야 최소 동전 수 구할 수 있음)

for i in arr:  # 그리디 적용
    value = K // i
    count += value
    K -= value * i
    if K == 0: break
        
print(count)
