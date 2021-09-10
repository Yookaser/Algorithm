# 17825. 주사위 윷놀이

def check(num):
    if 61<num<65:
        num -= 19
    elif 82<num<86:
        num -= 40
    elif num in {36, 55, 76}:
        num = 20
    return num


def game(idx, val, a, b, c, d):
    global ans
    if idx == 10:
        ans = max(ans, val)
        return
    for i, v in enumerate([a, b, c, d]):
        if v < 90:
            if v in {5, 10, 15}:
                x = check((v//2+1)*10 + A[idx])  # 5 => 30번대, 10 => 60번대, 15 => 80번대
            else:
                x = v + A[idx]
            
            if G[x] == 0:
                if i == 0: game(idx+1, val, 96, b, c, d)
                elif i == 1: game(idx+1, val, a, 97, c, d)
                elif i == 2: game(idx+1, val, a, b, 98, d)
                else: game(idx+1, val, a, b, c, 99)
            elif x not in (a, b, c, d):
                if i == 0: game(idx+1, val+G[x], x, b, c, d)
                elif i == 1: game(idx+1, val+G[x], a, x, c, d)
                elif i == 2: game(idx+1, val+G[x], a, b, x, d)
                else: game(idx+1, val+G[x], a, b, c, x)

    ans = max(ans, val)


A = list(map(int, input().split()))
G = [0] * 101
G[1:21] = [2 * i for i in range(1, 21)]
G[30:36] = [13, 16, 19]  # 13, 16, 19, 25, 30, 35, 40
G[60:65] = [22, 24]  # 22, 24, 25, 30, 35, 40
G[80:86] = [28, 27, 26]  # 28, 27, 26, 25, 30, 35, 40

ans = 0
game(0, 0, 0, 0, 0, 0)

print(ans)
