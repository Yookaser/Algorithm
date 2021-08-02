# 9095. 1, 2, 3 더하기

T = int(input())
sum_list = [0, 1, 2, 4] + [0] * 7 # 10까지의 수가 들어오므로 인덱스 10까지만

for i in range(4, len(sum_list)): # 범위 주의(i-3까지 더해야 함)
    sum_list[i] = sum_list[i-1] + (sum_list[i-2] + sum_list[i-3]) # 자기자신은 자기 이전 3개의 합이 규칙(DP문제)

for i in range(T):
    N = int(input())
    print(sum_list[N])