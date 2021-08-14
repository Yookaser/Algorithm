# 2564. 경비원

def coordinate(side, point): # (0, 0) ~ 입력 좌표의 최단 거리를 반환
    if side == 1: # 북쪽
        return point + col
    elif side == 2: # 남쪽
        return point + 0
    elif side == 3: # 서쪽
        return col - point
    else: # 동쪽
        return row + col - point
    

row, col = map(int, input().split())
stores = int(input())
arr = []

for i in range(stores):
    s1, p1 = map(int, input().split())
    arr.append((coordinate(s1, p1), s1)) # 원점부터 각 상점 좌표들의 최단 거리를 입력

side, point = map(int, input().split())
my = coordinate(side, point) # 원점부터 상근이의 최단 거리 입력 받음

result = 0
for i, j in arr:
    if (side in (1, 3) and j in (1, 3)) or (side in (2, 4) and j in (2, 4)): # 상근이와 상점이 둘 다 (서, 북), (동, 남)인 경우
        result += abs(my - i) # 결과에 각 원점부터 최단 거리의 절대값 차를 더함(최단 경로가 중복되는 부분이 있기 때문)
    else:
        move = my + i
        if move <= (row+col): # 최단 거리의 합이 (가로+세로)보다 작거나 같은 경우
            result += move # 원점을 경유한 경로로 지나가면 되므로 그냥 더함
        else: # 더 큰 경우
            result += (row+col) * 2 -move # 원점을 경유한 경로가 아닌 반대로 가는 게 더 이득이므로 지름에서 빼서 더해줌
print(result)