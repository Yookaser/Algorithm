# 15829. Hashing

def exponent(value, num): # 지수 계산 함수(그냥 지수곱하면 느리기 때문에 만든 함수, 단 num >=0 )
    if num == 0: # 0인 경우
        return 1
    elif num == 1: # 1인 경우
        return value
    
    cnt = 2 # 몇 번 제곱할 수 있는지 판단하기 위한 변수(ex - num이 10이면 3번 제곱하는 것을 판별)
    result = value # value 변수가 차후에 필요하기 때문에 만든 변수

    while True: # 몇 번 제곱할 수 있는지 판단
        if num // cnt >= 1: # 몫이 1보다 큰 경우
            result **= 2 # 처음엔 value 제곱이지만, 다음엔 제곱의 제곱과 같은 식으로 지속
            cnt *= 2 # cnt 값도 2배씩 증가해야 함(아니면 무한루프)
        else: # 몫이 1보다 작은 경우
            cnt //= 2 # cnt가 최종적으로 2배 커진 값으로 나오기 때문에 2로 나눠야 함(어차피 2의 배수이므로 몫으로 해도 됨)
            break
    
    return int(result * (value**(num - cnt))) # num이 2의 배수가 아닌 경우가 있기 때문에 (value**(num - cnt)) 부분이 필요함

hash_list = [None] + list('abcdefghijklmnopqrstuvwxyz') # 각 알파뱃의 인덱스 번호가 변환 값

N = int(input())
str_list = list(input())
result = 0

for i, j in enumerate(str_list):
    result += hash_list.index(j) * exponent(31, i)

print(result % 1234567891)