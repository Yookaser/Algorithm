import math
import sys
def dist(a, b):
    ax, ay = caseA[a]
    bx, by = caseB[b]
    return abs(ax - bx) + abs(ay - by)

def getMinDist():
    for i in range(W+1):
        for j in range(W+1):
            minVal = math.inf
            if i == j:
                continue
            elif i - j == -1 and i:
                for k in range(j-1):
                    now = dp[i][k] + dist(j, k)
                    if minVal > now and i != k:
                        minVal = now
                        trace[i][j] = [i, k]
                    elif minVal == now:
                        if dist(j, trace[i][j][1]) > dist(j, k):
                            trace[i][j] = [i, k]
                dp[i][j] = minVal
            elif i - j == 1 and j:
                for k in range(i-1):
                    now = dp[k][j] + dist(k, i)
                    if minVal > now and j != k:
                        minVal = now
                        trace[i][j] = [k, j]
                    elif minVal == now:
                        if dist(trace[i][j][0], i) > dist(k, i):
                            trace[i][j] = [k, j]
                dp[i][j] = minVal
            else:
                if i > j:
                    dp[i][j] = dp[i-1][j] + dist(i-1, i)
                    trace[i][j] = [i-1, j]
                else:
                    dp[i][j] = dp[i][j-1] + dist(j, j-1)
                    trace[i][j] = [i, j-1]
def traceDP(row, col):
    global res
    if row == col:
        return
    elif row < col:
        res.append(2)
    else:
        res.append(1)
    traceDP(trace[row][col][0],trace[row][col][1])

if  __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    I = sys.stdin.readline
    N, W = int(I()), int(I())
    caseA, caseB = [[1, 1]], [[N, N]]
    for i in range(W):
        a = list(map(int, input().split()))
        caseA.append(a)
        caseB.append(a)
    dp = [[0 for i in range(W+1)] for j in range(W+1)]
    trace = [[[0,0] for i in range(W+1)] for j in range(W+1)]
    getMinDist()
    minVal = math.inf
    row, col = math.inf, math.inf
    for i in range(W):
        if minVal > dp[W][i] and i != W:
            minVal = dp[W][i]
            row, col = W, i
        if minVal > dp[i][W] and i != W:
            minVal = dp[i][W]
            row, col = i, W
    print(minVal)
    res = []
    traceDP(row, col)
    for i in res[::-1]:
        print(i)

print(*dp, sep='\n')
