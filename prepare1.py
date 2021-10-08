# 1번
def solution(n):
    for i in range(1, n):
        if n % i == 1:
            break
    return i


# 2번
def solution(n, left, right):
    res = []
    
    for i in range(left, right+1):
        res.append(max(i%n+1, i//n+1))
    
    return res


# 3번
def solution(n, m, x, y, queries):
    ans = set()
    dx, dy = 0, 0
    for d, v in queries:
        if d == 0: dy += v
        elif d == 1: dy -= v
        elif d == 2: dx += v
        else: dx -= v
  
    if x == 0:
        if dx >= 0: row = [i for i in range(min(n, dx+1))]
        else: row = []
    elif x == n-1:
        if dx <= 0: row = [i for i in range(max(-n, dx), 1)]
        else: row = []
    else: row = [dx]

    if y == 0:
        if dy >= 0: col = [i for i in range(min(m, dy+1))]
        else: col = []
    elif y == m-1:
        if dy <= 0: col = [i for i in range(max(-m, dy), 1)]
        else: col = []
    else: col = [dy]

    for i in row:
        for j in col:
            if (-1<x+i<n) and (-1<y+j<m):
                ans.add((x+i, y+j))

    return len(ans)
