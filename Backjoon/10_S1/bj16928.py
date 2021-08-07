# 16928. 뱀과 사다리 게임

# 단순 함수 구현이지만, dfs보다 빠른 편임
def sl_game(idx):
    for dice in range(1, min(7, 101-idx)): # 주사위 반복(min(7, 101-idx)는 95이상 값일 경우를 위한 주사위값 설정)
        if idx + dice in ladder: # 사다리인 경우
            DP[ladder[idx+dice]] = min(DP[idx]+1, DP[idx+dice], DP[ladder[idx+dice]]) # 해당 사다리 이동 인덱스 값을 3개중 최소값 변경(밑 줄이랑 순서 중요할 것이라 생각)
            DP[idx+dice] = min(DP[idx]+1, DP[idx+dice]) # 해당 사다리 인덱스 값을 2개중 최소값으로 변경

        elif idx + dice in snake: # 뱀인 경우
            if DP[snake[idx+dice]] > DP[idx]+1: # 뱀을 타고 돌아간 경우가 해당 인덱스 값보다 작은 경우(2 1 // 2 60 // 40 98 // 65 25 가 있음 // => 엔터)
                DP[snake[idx+dice]] = DP[idx]+1
                return snake[idx+dice] # 해당 인덱스 값 반환(그러면 while에서 해당 인덱스부터 다시 반복 => 더 작은 값이 발견되었으므로 다시 반복해야 됨)

        else: # 사다리/뱀이 아닌 경우
            DP[idx+dice] = min(DP[idx]+1, DP[idx+dice])
            
N, M = map(int, input().split())
ladder = {} # 사다리 저장할 공간(해당 값이 있는지? 해당 값에서 어디로 가는지?만 필요하므로 딕셔너리 자료형 )
snake = {} # 뱀 저장할 공간(사다리와 같은 이유로 딕셔너리 자료형 선택)
DP = [0, 0] + [100] * 99 # 해당 인덱스 번호에 도달하기까지 최소 횟수가 저장될 공간(0, 1번은 0번이므로 0 고정)

for i in range(N): # 사다리 입력
    x, y = map(int, input().split())
    ladder[x] = y

for i in range(M): # 뱀 입력
    x, y = map(int, input().split())
    snake[x] = y

state = 1 # 현재 상태(1~100)
while state <= 99:
    value = sl_game(state) # 입력값 반환 받음(None or 인덱스 번호)
    if value: # 인덱스 번호인 경우
        state = value # state는 반환값으로 저장. 해당 값부터 돌 것(뱀을 탔을 때, 더 빠른 경우임)
    else: # None인 경우
        state += 1 # 특이사항 없으므로 +1

print(DP[-1]) # 100번째 인덱스 출력