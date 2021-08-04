# 16928. 뱀과 사다리 게임

def dice(idx):
    confirm[idx] = True

    for i in range(1, min(7, 101-idx)):
        if not confirm[idx+i]:
            if DP[idx+i] == -1:
                print(i, idx, idx+i, DP[idx+i])
                print(DP[ladder_snake[idx+i]])
                DP[idx+i] = DP[ladder_snake[idx+i]]= min(DP[idx]+1, DP[idx+i], DP[ladder_snake[idx+i]])
            else:
                DP[idx+i] = min(DP[idx]+1, DP[idx+i])
                confirm[idx+i] = True

N, M = map(int, input().split())
ladder_snake = {}
DP = [0, 0] + [100] * 99
confirm = [False] * 101

for i in range(N+M):
    x, y = map(int, input().split())
    DP[x] = -1
    ladder_snake[x] = y
print(DP[62])
for i in range(1, 100):
    dice(i)

print(DP[6], DP[12], DP[98], DP[100])
print(DP[-1])