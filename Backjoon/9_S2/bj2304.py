# 2304. 창고 다각형

N = int(input())
row_arr, col_arr = [], [] # row, col 인덱스를 저장할 리스트
max_height = 0 # 최대 높이
idx_max = 0 # 최대 높이의 인덱스

for _ in range(N):
    row, col = map(int, input().split())
    row_arr.append(row)
    col_arr.append(col)
    if col > max_height:
        max_height = col
        idx_max = row

sort_arr = sorted(row_arr)
start, mid, end = sort_arr[0], idx_max, sort_arr[-1] # 시작, 중간(최대 높이 인덱스), 끝
height, result = 0, 0 # 높이, 결과 초기화

for i in range(start, mid+1): # 시작 ~ 중간 인덱스
    if i in row_arr and col_arr[row_arr.index(i)] > height:
        height = col_arr[row_arr.index(i)] # 더 높은 것이 나올때마다 높이 교체
    result += height # 높이만큼 더하기

height = 0 # 높이 초기화
for i in range(end, mid, -1): # 끝 ~ 중간+1 인덱스
    if i in row_arr and col_arr[row_arr.index(i)] > height:
        height = col_arr[row_arr.index(i)] # 더 높은 것이 나올때마다 높이 교체
    result += height # 높이만큼 더하기

print(result)