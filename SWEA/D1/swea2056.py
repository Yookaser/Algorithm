# 2056. 연월일 달력

def right_data(Num):
    month = int(Num[4:6])
    date = int(Num[6:])

    if not (month in range(1,13)):
        return -1
    else:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if not (date in range(1,32)):
                return -1
        elif month in [4, 6, 9, 11]:
            if not (date in range(1,31)):
                return -1
        else:
            if not (date in range(1,29)):
                return -1
    
    solu = Num[:4] + '/' + Num[4:6] + '/' + Num[6:]
    
    return solu

T = int(input())

for _ in range(T):
    N = input()
    solu = right_data(N)
    print(f'#{_ + 1} {solu}')