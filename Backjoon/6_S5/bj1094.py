# 1094. 막대기
import math

def many_cut(num):
    stick = 64

    if stick == num: # 시작부터 같을 경우
        return 1

    while True: # 막대기가 1개 이상될 때까지 반복
        if stick/2 > num:
            stick = int(stick/2)
        elif int(stick/2) == num:
            return 1
        else:
            break
    
    sticks = [stick] # 막대기들을 저장할 공간

    while sum(sticks) != num:
        cut = min(sticks)

        if sum(sticks) - cut/2 > num:
            sticks.append(int(cut/2))
            sticks.remove(cut)
        elif math.isclose(sum(sticks) - cut/2,num):
            return len(sticks)
        else:
            sticks.append(int(cut/2))
            sticks.append(int(cut/2))
            sticks.remove(cut)

X = int(input())

print(many_cut(X))