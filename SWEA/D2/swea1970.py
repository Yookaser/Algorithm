# 1970. 쉬운 거스름돈

def change_money(money):
    result = [0] * 8  # 결과를 저장할 공간
    changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for i in range(8):
        result[i] += money // changes[i]  # 큰 수부터 나눈 몫을 result에 저장
        money -= changes[i] * (money // changes[i])  # money에서 해당 (금액 * 몫)만큼 빼기
    
    return result


T = int(input())
for _ in range(T):
    N = int(input())
    
    print(f'#{_ + 1} ')
    print(*change_money(N))
