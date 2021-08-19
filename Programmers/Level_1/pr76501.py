# 76501. 음양 더하기

def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]: answer += absolutes[i] # True인 경우
        else: answer -= absolutes[i] # False인 경우
    return answer