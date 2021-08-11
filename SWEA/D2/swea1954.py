# 1954. 달팽이 숫자

# 방법1.
def snail_number(num):
    arr = list(range(1, num + 1)) + list(range(1, num)) # 배열 만들기(각 방향에 규칙으로)
    arr.sort(reverse=True) # 역순 정렬
    result = [[0] * num for _ in range(num)] # 결과를 저장할 2차원 리스트
    row, col, cnt = [0, -1, 0] # 행, 열, 입력값 초기화(열은 처음에 더해지므로 -1로 지정)

    for i in range(len(arr)): # arr의 길이 반복(방향의 갯수를 의미)
        for j in range(arr[i]): # arr의 요소만큼 반복(방향으로 몇 칸 나아가는지 의미)
            if i % 4 == 0: # 오른쪽인 경우
                col += 1 # 첫번째 방향이므로 제일 처음 걸리는 조건임(따라서 col 초기값 -1)
            elif i % 4 == 1: # 아래인 경우
                row += 1 # 두번째 방향임(따라서 row 초기값 0)
            elif i % 4 == 2: # 왼쪽인 경우
                col -= 1
            else: # 위쪽인 경우
                row -= 1
            cnt += 1 # 하나씩 증가해야함(따라서 cnt 초기값 0으로 함)
            result[row][col] = cnt # 해당 좌표(row, col)에 값(cnt) 입력
    return result

T = int(input())

for test in range(T):
    N = int(input())
    result = snail_number(N)

    print('#{}'.format(test+1))
    for numbers in result:
        print(*numbers)

# 방법2.
def landsnail_number(num):
    cnt = 1 # 리스트에 들어갈 숫자
    direction = 0 # 리스트의 진행 방향(0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽)
    result = [[0] * num for _ in range(num)] # 달팽이 숫자를 저장할 공간
   
    for i in range(1, num*2): # 총 방향은 num * 2 - 1개가 나와야 함(여기서 1부터 시작한 것은 j의 범위 조건 때문)
        for j in range(num - int(i/2)): # 방향을 진행할수록 해당 방향으로 가는 횟수는 작아져야 함
            d = direction // 4 # 가독성을 위한 변수
            
            if direction % 4 == 0: # 오른쪽일 때(방향이 계속 증가하므로 나머지로 구함)
                result[d][j + d] = cnt
                cnt += 1
            
            elif direction % 4 == 1: # 아래쪽일 때
                result[j + 1 + d][(num-1) - d] = cnt
                cnt += 1
            
            elif direction % 4 == 2: # 왼쪽일 때
                result[(num-1) - d][(num - 1) - d - (j + 1)] = cnt
                cnt += 1
                
            elif direction % 4 == 3: # 위쪽일 때
                result[(num- 1) - d - (j+1)][d] = cnt
                cnt += 1

        direction += 1 # 방향은 계속 증가해야 함(그래야 인덱스를 찾을 수 있음)

    return result

T = int(input())

for _ in range(T):
    N = int(input())
    solu = landsnail_number(N)

    print(f'#{_ + 1}')
    for i in range(N):
        print(*solu[i])