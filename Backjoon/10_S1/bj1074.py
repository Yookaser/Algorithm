# 1074. Z

def plan_z(row_first, col_first, size, row, col): # 행 시작값, 열 시작값, 크기, 찾는 행, 찾는 열
    if size == 1: # Base Case는 size가 1일 때, size는 매번 재귀마다 2로 나눠짐(2의 배수이므로 // 사용함)
        return size # 1 반환
    weight = 0 # 가중치(박스?를 4등분 한다고 했을 때, 0: 왼쪽 위, 1: 오른쪽 위, 2: 왼쪽 아래, 3: 오른쪽 아래)

    if row_first <= row < row_first + size//2 and col_first <= col < col_first + size//2: # 찾는 것이 왼쪽 위인 경우
        weight = 0 # 가중치 수정

    elif row_first <= row < row_first + size//2 and col_first + size//2 <= col < col_first + size: # 찾는 것이 오른쪽 위인 경우
        weight = 1
        col_first += size//2 # 열 시작값 수정(다음 재귀를 위해)

    elif row_first + size//2 <= row < row_first + size and col_first <= col < col_first + size//2: # 찾는 값이 왼쪽 아래인 경우
        weight = 2
        row_first += size//2 # 행 시작값 수정(다음 재귀를 위해)

    elif row_first + size//2 <= row < row_first + size and col_first + size//2 <= col < col_first + size: # 찾는 값이 오른쪽 아래인 경우
        weight = 3
        row_first += size//2
        col_first += size//2

    return weight * (size**2)//4 + plan_z(row_first, col_first, size//2, row, col) # 재귀식(weight * (size**2)//4는 순서를 찾기 위함)

N, r, c = list(map(int, input().split()))

print(plan_z(0, 0, 2**N, r, c) - 1) # 결과값은 +1되서 나오므로 -1 해야 함(문제는 첫 시작값을 0으로 봄)