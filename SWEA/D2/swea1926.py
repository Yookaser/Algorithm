# 1926. 간단한 369게임

def game_369(num):
    result = list(map(str, range(1, num + 1)))

    for idx, value in enumerate(result):
        cnt = 0
        if '3' in value or '6' in value or '9' in value: # 3, 6, 9가 속하는 경우
            cnt += value.count('3') # 3 count
            cnt += value.count('6') # 6 count
            cnt += value.count('9') # 9 count
            result[idx] = '-' * cnt # 변환

    return result

N = int(input())

print(*game_369(N))