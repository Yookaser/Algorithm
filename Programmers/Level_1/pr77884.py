# 77884. 약수의 개수와 덧셈

# 방법1.

def solution(left, right):
    answer = 0
    for num in range(left, right+1): # left~right
        cnt = 1
        for i in range(1, num):
            if num % i == 0: # 약수인 경우
                cnt += 1 # 개수 +1
        if cnt % 2: # 약수의 개수가 홀수인 경우
            answer -= num
        else: # 짝수인 경우
            answer += num
    return answer

# 방법2.

def solution(left, right):
    answer = 0
    for num in range(left, right+1): # left~right
        if int(num**0.5) == num**0.5: # 제곱수이면 약수가 홀수개
            answer -= num
        else: # 제곱수가 아니면 약수가 짝수개
            answer += num
    return answer