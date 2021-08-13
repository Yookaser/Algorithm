# 2628. 종이자르기

C, R = map(int, input().split())
cut = int(input())
row, col = [0, R], [0, C] # 크게 보면 주어진 직사각형도 잘려진 것!

for _ in range(cut): # cut한 부분 row와 col로 나눠 받기
    rc, num = map(int, input().split())
    if rc:
        col.append(num)
    else:
        row.append(num)

row.sort() # 정렬 필요
col.sort()

row_result, result = [], [] # 가로를 자른 결과를 저장, 최종 결과를 저장
for i in range(1, len(row)): # 가로를 먼저 자르기
    row_result.append((row[i] - row[i-1])*C)

for area in row_result: # 가로 자른 결과
    for i in range(1, len(col)): # 세로로 자르기
        result.append(int((col[i] - col[i-1])/C*area)) # 세로는 나눠진 비율을 계산해야 함

print(max(result))