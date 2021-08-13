# 2578. 빙고

def isPrise():
    result = 0 # 빙고 카운팅

    for i in bingo_map: # 행 검사
        cnt = 0
        for j in i:
            if j in bingo:
                cnt += 1
        if cnt == 5: # 한 행이 빙고인 경우
            result += 1
    
    for i in zip(*bingo_map): # 열 검사
        cnt = 0
        for j in i:
            if j in bingo:
                cnt += 1
        if cnt == 5: # 한 열이 빙고인 경우
            result += 1

    cnt, cnt1 = 0, 0
    for i in range(5):
        if bingo_map[i][4-i] in bingo: # 우상향 대각선
            cnt += 1
        if bingo_map[i][i] in bingo: # 우하향 대각선
            cnt1 += 1
    
    if cnt == 5: # 우상향 대각선이 빙고인 경우
        result += 1
    if cnt1 == 5: # 우하향 대각선이 빙고인 경우
        result += 1
    
    if result >= 3: # 3 이상인 경우(부등호여야 함)
        return True
    else:
        return False

bingo_map = [list(map(int, input().split())) for _ in range(5)] # 빙고맵
numbers = sum([list(map(int, input().split())) for _ in range(5)], []) # 사회자가 부르는 번호(입력받고 일렬로 만듬)
bingo = set(numbers[:4]) # 4까지는 빙고가 없으므로 미리 입력(집합은 in 연산 속도의 이유로 사용)

for i in range(4, 25):
    bingo.add(numbers[i])
    if isPrise():
        print(i+1) # i는 인덱스이므로 +1
        break