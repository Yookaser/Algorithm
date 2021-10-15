# 2618. 경찰차

from sys import stdin, setrecursionlimit


def dist(a, b):  # 거리를 구하는 함수
    if b == 0: bx = by = N  # 만약, b가 0인 경우(처음 위치인 N에서 시작해야 함)
    else: bx, by = A[b]
    ax, ay = A[a]
    return abs(ax-bx) + abs(ay-by)


def getDP():  # DP를 구하는 함수
    for a in range(W+1):
        for b in range(W+1):
            if a == b or DP[a][b]: continue

            if abs(a-b) == 1 and a and b:  # 둘의 차이가 1인 경우(바로 전에 어디서 온지 알 수 없으므로 모든 경우를 찾아야 함)
                t = 10**7
                if b > a:  # b - a == 1인 경우(즉, b가 새로 갱신된 것)
                    for c in range(a):
                        cur = DP[a][c] + dist(b, c)  # 순서 중요(c가 0인 경우가 있기 때문)
                        if t > cur:  # 최솟값 갱신
                            t = cur
                            BDP[a][b] = (a, c)  # 추적을 위해 (a,b) 좌표는 (a,c) 좌표에서 왔음을 표시
                        elif t == cur and dist(b, BDP[a][b][1]) > cur - DP[a][c]:  # 만약, 거리가 더 짧은 경우
                            BDP[a][b] = (a, c)
                    
                else:  # a - b == 1인 경우(즉, a가 새로 갱신된 것)
                    for c in range(b):
                        cur = DP[c][b] + dist(c, a)
                        if t > cur:
                            t = cur
                            BDP[a][b] = (c, b)
                        elif t == cur and dist(BDP[a][b][0], a) > cur - DP[c][b]:
                            BDP[a][b] = (c, b)
                DP[a][b] = t  # 최종 갱신
            elif a > b:  # a가 더 큰 경우(바로 전인 a-1에서 온 것)
                DP[a][b] = DP[a-1][b] + dist(a-1, a)  # 순서 중요(a-1이 뒤로 오면 안됨 => 0인 경우가 있기 때문)
                BDP[a][b] = (a-1, b)
            else:  # b가 더 큰 경우(바로 전인 b-1에서 온 것)
                DP[a][b] = DP[a][b-1] + dist(b, b-1)  # 순서 중요(b-1이 뒤로 가야함)
                BDP[a][b] = (a, b-1)
    
    m = 10**6
    for i in range(W):  # 가장 작은 좌표와 값을 찾기 위해 반복
        if m > DP[W][i]:
            m = DP[W][i]
            x, y = W, i
        if m > DP[i][W]:
            m = DP[i][W]
            x, y = i, W
    return m, x, y


def backDP(x, y):  # 어떤 좌표에서 왔는지 찾아가는 함수
    if x == y: return  # base case
    elif x < y: ans.append(2)
    else: ans.append(1)
    backDP(BDP[x][y][0], BDP[x][y][1])


input = stdin.readline
setrecursionlimit(10**5)
N, W = int(input()), int(input())
A = [(1,1)] + [tuple(map(int, input().split())) for _ in range(W)]

DP = [[0]*(W+1) for _ in range(W+1)]  # A(행), B(열)의 인덱스는 각각 두 경찰차가 가장 마지막에 출동한 것(즉, (4,3)이면 A=4, B=3을 마지막으로 출동한 것)
BDP = [[(0, 0) for _ in range(W+1)] for _ in range(W+1)]  # 추적을 위한 DP((4,3) 위치에 (2,4)가 있다면 (2,4) => (4,3)으로 왔다는 의미)

ans = []
m, x, y = getDP()
backDP(x, y)

print(m)
print(*ans[::-1], sep='\n')
