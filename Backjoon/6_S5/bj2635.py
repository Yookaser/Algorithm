# 2635. 수 이어가기

N = int(input())
result = 0
result_list = []

for i in range(N, 0, -1): # N~1까지 -1씩 증가
    arr = [N, i] # 초기값 넣어줘야 함
    while arr[-2] - arr[-1] > -1:
        arr.append(arr[-2] - arr[-1])
    if len(arr) > result: # 기존 result와 비교(등호는 안 넣는게 계산량 적어짐)
        result = len(arr)
        result_list = arr[:] # 얕은 복사

print(result)
print(*result_list)
