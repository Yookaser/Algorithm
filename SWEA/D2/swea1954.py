# 1954. 달팽이 숫자

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