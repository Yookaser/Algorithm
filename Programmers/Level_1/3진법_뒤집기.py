# 3진법 뒤집기

def solution(n):
    change = '' # 3진법 변환을 저장할 변수
    result = 0 # 결과를 저장할 변수

    while n > 0: # n이 0보다 클 때, 반복
        change += str(n % 3) # 나머지를 저장(거꾸로 저장됨 -> 다시 거꾸로 변환 필요 X)
        n //= 3 # 몫만 저장
    
    for idx, value in enumerate(list(change)[::-1]):
        if int(value): # value 값이 True인 경우
            result += int(value) * (3**idx) # 10진수로 변환
        
    return result