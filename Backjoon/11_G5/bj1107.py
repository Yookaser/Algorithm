# 1107. 리모컨

# 브루트 포스(채널 값이 500000이고, 고장난 키 확인했는지 아닌지 판단하는 횟수가 최악 10번이므로, 반복은 약 5백만 -> 브루트 포스 가능하다 판단)
def mini_click(channel, trouble_set):
    if channel in range(97, 105): # 97 ~ 105는 굳이 밑의 알고리즘이 필요 없음(기본 채널값이 100이므로)
        return abs(channel - 100) # 간단하게 차이 절대값 반환

    close_number = 100 # 기본 채널 값으로 설정(이거 다른 값 하면 제대로 결과 안 나올 수 있음)
    for number in list(range(0, 1000001)): # 근접한 수 찾기 위한 반복문(들어올 수 있는 채널값이 0~500000이므로 최대값을 500000 + 500000으로 잡음)
        for state in str(number): # 해당 숫자가 고장난 키에 속하는지 확인하기 위한 반복문
            if int(state) in trouble_set:
                break # 속하면 break 걸어서 else문 안 거치게
        else: # 만약 고장난 키가 없다면
            if abs(channel - close_number) > abs(channel - number): # 새로운 number가 기존 근접수보다 채널에 가까운지 판단
                close_number = number # 가깝다면 근접수 갱신
    
    if close_number != 100: # 근접수가 100이 아니면(갱신됐다면)
        result = abs(channel - close_number) + len(str(close_number)) # 채널 번호 입력하는 것 고려해야 함
    else: # 근접수가 100이라면
        result = abs(channel - close_number) # 채널 번호 고려할 필요 없음

    return result

channel = int(input())
trouble = int(input())

if trouble: # trouble이 1~10인 경우
    trouble_set = set(map(int, input().split())) # 집합이 리스트보다 더 빠르다고, 알고 있어서 집합 사용
else: # trouble이 0인 경우(이거 지정 안해주면, 함수 불러올 때 trouble_set값 없다며 오류나게 됨(함수 기본값 지정해도 오류 생김))
    trouble_set = {}

print(mini_click(channel, trouble_set))