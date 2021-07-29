# 1989. 초심자의 회문 검사

T = int(input())

for _ in range(T):
    arr = list(input())
    if arr == arr[::-1]: # 뒤로 읽어도 같은 경우([::-1]의 슬라이싱으로 꺼꾸로 만들기)
        print(f'{_ + 1} 1')
    else:
        print(f'{_ + 1} 0')