# 1945. 간단한 소인수분해

def Decomposition(Num):
    
    for i in prime_number:
        while Num % i == 0:
            prime_number[i] += 1
            Num = int(Num/i)

    solu = list(prime_number.values()) # 딕셔너리의 values를 출력하면 다른 형태로 나오므로 list로 형변환
    return solu

T = int(input())

for _ in range(T):
    prime_number = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0} # Key = 소수, value = 갯수로 활용
    N = int(input())
    print(f'#{_ + 1}', *Decomposition(N)) # dict의 values를 원하는 형태로 출력하기 위해 출력 구분