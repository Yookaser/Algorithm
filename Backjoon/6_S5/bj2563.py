# 2563. 색종이

N = int(input())
arr = [[0] * 101 for _ in range(101)]  # 인덱스 계산의 편리성을 위해 101까지

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):  # 해당 좌표 값 1로 변환(sum을 위해서)
        for j in range(y, y+10):
            arr[i][j] = 1

print(sum(sum(arr, [])))  # 합계 구하기