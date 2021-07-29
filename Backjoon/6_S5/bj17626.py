# 17626. Four Squares

# 방법1. 브루트 포스
N = int(input())
cnt = 4 # 초기값을 문제상 최대값인 4로 지정

for first in range(int(N**0.5), int(N**0.5//2), -1): # 첫 번째 숫자 제곱(범위는 거꾸로! 최소도 지정(second보다 작을 필요 없음))
    temp1 = N - first**2
    if temp1 != 0: # first에서 안 끝나는 경우
        for second in range(int(temp1**0.5), int(temp1**0.5//2), -1): # 두 번째 숫자 제곱(범위 지정으로 시간 단축)
            temp2 = temp1 - second**2
            if temp2 != 0: # second에서 안 끝나는 경우
                for third in range(int(temp2**0.5), int(temp2**0.5//2), -1): # 세 번째 숫자 제곱(범위 지정으로 시간 단축)
                    temp3 = temp2 - third**2
                    if temp3 == 0: # third에서 끝난 경우(만약, 안 끝나면 그냥 초기 cnt 출력하면 됨)
                        cnt = min(cnt, 3)
                        break # third에서 끝났다면, 해당 for문 더 돌필요가 없음
            else:
                cnt = min(cnt, 2)
                break # second에서 끝났다면, 해당 for문 더 돌필요가 없음
    else:
        cnt = min(cnt, 1)
        break # first에서 끝났다면, 해당 for문 더 돌필요가 없음
print(cnt)

# 방법2. 점화식(DP)(pyp3)
# N = int(input())

# dp = [0, 1] + [4] * (N - 1) # 점화식 미리 생성(0은 4, 9같은 제곱수의 횟수를 위해서, 2이상은 일단 최대값 4로 설정)

# for i in range(2, N + 1): # N까지 순환하게
#     cnt = 1 # 초기값은 1

#     while i >= cnt**2:
#         dp[i] = min(dp[i], dp[i - cnt**2]) # 최소값은 결국 (i - cnt**2)번째 갯수에서 + 1한 것과 동일해짐(+ 1은 아래서 실행)
#         cnt += 1
    
#     dp[i] += 1 # + 1은 여기서 실행(위에서 하면 안됨! 위에서 하면 계속 정답보다 1씩 큰 수가 나오게 됨)

# print(dp[N])