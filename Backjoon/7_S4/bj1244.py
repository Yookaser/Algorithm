# 1244. 스위치

number = int(input()) + 1 # 인덱스를 편하게 받기 위해 +1
switch = [0] + list(map(int, input().split())) # 인덱스를 편하게 받기 위해 [0] 추가
student = int(input())

for i in range(student):
    s, n = map(int, input().split())

    if s == 1: # 남학생
        temp = 1 # 배수로 사용할 변수
        while 1:
            if n*temp < number: # 인덱스 내일때만(단, 등호는 들어가면 안됨)
                switch[n*temp] = int(not switch[n*temp]) # 0 -> 1, 1 -> 0 변환(딕셔너리 써도 됨)
            else: # 인덱스 벗어난 경우
                break
            temp += 1
    else: # 여학생
        temp = 1 # 배수로 사용할 변수
        switch[n] = int(not switch[n]) # 자기자신은 무조건 바꾸므로 미리 바꿈
        while 1:
            if n-temp in range(1, number) and n+temp in range(1, number) and switch[n-temp] == switch[n+temp]:
                switch[n-temp] = int(not switch[n-temp])
                switch[n+temp] = int(not switch[n+temp])
            else:
                break
            temp += 1

del switch[0] # 추가했던 0 제거(출력을 편하게 하기 위해서)

for i in range(0, number-1, 20): # 0인덱스 지웠으므로 number-1
    print(*switch[i:i+20])
