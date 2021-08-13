# 10157. 자리배정

def sitDown(row, col, num):
    state = 0 # 현재 값
    state_row, state_col = 1, 0 # 시작 row, col(row는 col 먼저 움직이므로 초기값을 1로 잡음)
    cnt_row, cnt_col = 0, 0 # 지나온 row, col의 수가 될 것(방향의 개수를 의미)

    while 1:
        if num > state + (col-cnt_row): # 위쪽으로 이동할 때, 한 번에 이동 가능한 경우
            state += col - cnt_row # 현재 값 움직임
            state_col += col - cnt_col # 현재 col값 움직임
            cnt_col += 1 # 지나온 col수 +1
        else: # 이동 불가능한 경우(한 번에 이동 불가능한 것, 해당 방향의 숫자 개수보다 적은 수는 움직일 수 있음)
            return state_row, state_col + (num-state) # 목표 - 현재 값의 차이만큼 더 이동함

        if num > state + (row-cnt_col): # 오른쪽으로 이동할 때, 한 번에 이동 가능한 경우
            state += row - cnt_col
            state_row += row - cnt_col
            cnt_row += 1
        else:
            return state_row + (num-state), state_col
        
        if num > state + (col-cnt_row): # 아래쪽으로 이동할 때, 한 번에 이동 가능한 경우
            state += col - cnt_row
            state_col -= col - cnt_row
            cnt_col += 1
        else:
            return state_row, state_col - (num-state)
        
        if num > state + (row-cnt_col): # 왼쪽으로 이동할 때, 한 번에 이동 가능한 경우
            state += row - cnt_col
            state_row -= row - cnt_col
            cnt_row += 1
        else:
            return state_row - (num-state), state_col
            
C, R = map(int, input().split())
K = int(input())
if K > C*R: # 자리배정 불가능한 값인 경우
    print(0)
else:
    print(*sitDown(C, R, K))