# 17825. 주사위 윷놀이

def check(num):  # 인덱스를 조정하는 함수
    if 61<num<65:
        num -= 29
    elif 82<num<86:
        num -= 50
    elif num in {36, 65, 86}:
        num = 20
    return num


def game(idx, val, a, b, c, d):
    global ans
    if idx == 10:  # base case
        ans = max(ans, val)
        return

    # print(idx, val, a, b, c, d)
    for i, v in enumerate([a, b, c, d]):  # i는 a, b, c, d 중 누구인지 구분하기 위함
        if v < 90:  # 도착한 말
            if v in {5, 10, 15}:  # 지름길에 있는 경우
                x = check((v//2+1)*10 + A[idx] - 1)  # 5 => 30번대, 10 => 60번대, 15 => 80번대(-1은 인덱스를 처리하기 위함)
            else:
                x = v + A[idx]
            
            if G[x] == 0:  # 0인 경우는 2가지의 경우 => 1. 도착함, 2. 중복된 경로임(25 ~ 40)
                x = check(x)  # 인덱스 조정(위의 2가지 경우를 구분하기 위함 AND 말이 중복되어 있지 않게 하기 위함)

            if G[x] == 0:  # 도착한 경우
                if i == 0: game(idx+1, val, 96, b, c, d)  # a = 96(중복되지 않게)
                elif i == 1: game(idx+1, val, a, 97, c, d)  # b = 97
                elif i == 2: game(idx+1, val, a, b, 98, d)  # c = 98
                else: game(idx+1, val, a, b, c, 99)  # d = 99
            elif x not in (a, b, c, d):  # 도착하지 않았는데, 중복되지 않는 경우
                if i == 0: game(idx+1, val+G[x], x, b, c, d)
                elif i == 1: game(idx+1, val+G[x], a, x, c, d)
                elif i == 2: game(idx+1, val+G[x], a, b, x, d)
                else: game(idx+1, val+G[x], a, b, c, x)

    ans = max(ans, val)  # 주사위 10번을 다 돌기 전에 끝날 수 있으므로 추가


A = list(map(int, input().split()))
G = [0] * 101
G[1:21] = [2 * i for i in range(1, 21)]
G[30:36] = [13, 16, 19, 25, 30, 35]  # 13, 16, 19, 25, 30, 35, 40
G[60:65] = [22, 24]  # 22, 24, 25, 30, 35, 40
G[80:86] = [28, 27, 26]  # 28, 27, 26, 25, 30, 35, 40

ans = 0
game(0, 0, 0, 0, 0, 0)  # 인덱스, 합계, 1번 말, 2번 말, 3번 말, 4번 말

print(ans)
