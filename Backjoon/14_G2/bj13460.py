# 13460. 구슬 탈출 2

def tiltLeft():
    return

N, M = map(int, input().split())
arr = [list(map(str, list(input()))) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'B':
            bx, by = i, j
        elif arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'O':
            ox, oy = i, j

print(bx, by, rx, ry, ox, oy)
print(*arr, sep='\n')