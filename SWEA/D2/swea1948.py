# 1948. 날짜 계산기

def cal_date(month1, date1, month2, date2):
    if month1 == month2: # 같은 달일 때
        solu = date2 - date1 + 1 # 날짜의 차를 계산할 때는 +1 해야 함
        return solu
    else: # 다른 달일 때
        solu = (month_list[month1] - date1) + (date2) + 1 # 첫 번째 달의 일 수 + 두 번째 달의 일 수 + 1

        for i in range(month1 + 1, month2): # 첫 번째, 두 번째 달 이외의 달이 있을 경우
            solu += month_list[i]

        return solu

month_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 각 달의 마지막 일 수를 표현하는 공간
T = int(input())

for _ in range(T):
    solu = 0
    month1, date1, month2, date2 = list(map(int, input().split()))
    print(f'#{_ + 1} {cal_date(month1, date1, month2, date2)}')