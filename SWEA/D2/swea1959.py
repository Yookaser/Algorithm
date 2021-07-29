# 1959. 두 개의 숫자열

def cal_list(arr1, arr2): # arr2 배열 길이가 더 짧은 경우로 가정
    dp = [0] * (len(arr1) - len(arr2) + 1) # 두 배열 곲의 값을 저장할 공간

    for _ in range(len(arr1) - len(arr2) + 1): # 두 배열의 곱을 몇 번 반복할지
        total = 0 # 곱의 값 저장할 변수

        for i in range(len(arr2)): # 두 배열의 곱을 실행
            total += arr1[_ + i] * arr2[i]

        dp[_] = total # 곱의 값을 저장

    return max(dp)

        

T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split()))
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    if len(A_list) > len(B_list):
        print(f'#{_ + 1} {cal_list(A_list, B_list)}')
    else:
        print(f'#{_ + 1} {cal_list(B_list, A_list)}')