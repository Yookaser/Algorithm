# 1288. 새로운 불면증 치료법

def sheep_number(Num):
    arr = [0] * 10 # 0 ~ 9의 각 자리수를 표현하는 공간
    change_Num = Num # 원본 Num은 보존해야 하므로, 대신 변경될 변수
    count = 0 # 몇 번째인지, 몇을 곱할지 결정하는 변수

    while 0 in arr:
        Num_list = list(map(int, list(str(change_Num)))) # 각 자리수를 리스트의 인자로 변환하기 위해

        for i in Num_list:
            arr[i] += 1 # 각 자리수를 더해줌
        count += 1
        change_Num = Num * (count + 1)

    return count * Num

T = int(input())

for _ in range(T):
    N = int(input())
    print(f'#{_ + 1} {sheep_number(N)}')