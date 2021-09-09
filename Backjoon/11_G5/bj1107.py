# 1107. 리모컨

# 브루트 포스(채널 값이 500000이고, 고장난 키 확인했는지 아닌지 판단하는 횟수가 최악 10번이므로, 반복은 약 5백만 -> 브루트 포스 가능하다 판단)
def digits(num):
    if num == 0: return [0]
    res = []
    while num:
        res.append(num % 10)
        num //= 10
    return res


def mini_click(c, t):
    if c in range(97, 105):  # 97 ~ 105는 굳이 밑의 과정이 불필요
        return abs(c - 100)  # 절대값 반환

    ans, val = abs(100-c), 100
    for n in list(range(0, 1000001)):  # 근접한 수 찾기 위한 반복문(들어올 수 있는 채널값이 0~500000이므로 최대값을 500000 + 500000으로 잡음)
        if ans > abs(c-n):
            for state in digits(n):  # 해당 숫자가 고장난 키에 속하는지 확인하기 위한 반복문
                if state in t:
                    break
            else:  # 만약 고장난 키가 없다면
                if ans > abs(c - n):
                    ans = abs(c - n)  # 가깝다면 근접수 갱신
                    val = n
    
    return min(abs(100-c), abs(val-c) + len(str(val)))


channel = int(input())
trouble = int(input())

if trouble:
    trouble_set = set(map(int, input().split()))
else:  # trouble이 0인 경우
    trouble_set = {}

print(mini_click(channel, trouble_set))
