# 1259. 팰린드롬수

while True:
    N = input() # 입력값을 그대로 받음(str)

    if int(N) == 0: # 0인 경우
        break

    else:
        if N == N[::-1]: # 역순과 같은 경우
            print('yes')
        else: # 역순과 다른 경우
            print('no')