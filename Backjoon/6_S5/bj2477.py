# 2477. 참외밭

N = int(input())
direction, length = [], [] # direction: 방향만 저장, length: 길이만 저장
big, small = 1, 1 # 큰 박스에서 작은 박스를 뺄 것

for _ in range(6): # 입력 받기
    dist, side = map(int, input().split())
    direction.append(dist)
    length.append(side)

for i in range(1, 5): # 방향 1~4 순회
    if direction.count(i) == 1: # 가장 큰 변인 경우(방향이 1개인 것은 가장 긴 변)
        idx = direction.index(i) # 인덱스 추출
        big *= length[idx] # 가장 긴 변이므로 큰 박스에 곱셈
        small *= length[(idx+3)%6] # 가장 긴 변에서 3칸 이동(반시계)하면, 빼야하는 변의 길이 중 하나가 나옴

print((big-small)*N)