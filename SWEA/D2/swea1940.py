# 1940. 가랏! RC카!

def RC_car(total_speed, total_distance, command, speed = 0): # 입력값이 1개일 경우 speed값을 고정하기 위해
    if command == 0:
        return total_speed, total_distance + total_speed
    elif command == 1:
        return total_speed + speed, total_distance + (total_speed + speed)
    else:
        return max(total_speed - speed, 0), max(total_distance + (total_speed - speed), 0) # (거리, 속도)가 0보다 작으면 안됨

T = int(input())

for _ in range(T):
    total_speed = 0 # 현재 스피드를 의미하는 변수
    total_distance = 0 # 총 움직인 거리를 의미하는 변수

    for i in range(int(input())):
        arr = list(map(int, input().split())) # command가 0인 경우 speed가 주어지지 않음(즉, 입력값이 달라짐)
        
        if len(arr) == 1: # 입력값이 1개인 경우(command가 0인 경우)
            total_speed, total_distance = RC_car(total_speed, total_distance, arr[0])
        else: # 입력값이 2개인 경우(command가 0이 아닌 경우)
            total_speed, total_distance = RC_car(total_speed, total_distance, arr[0], arr[1])
            
    print(f'#{_ + 1} {total_distance}')