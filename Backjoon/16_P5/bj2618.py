# 2618. 경찰차

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


input = __import__('sys').stdin.readline
N, W = int(input()), int(input())
A = [(0,0)] + [tuple(map(int, input().split())) for _ in range(W)]

DP = [[0]*(W+1) for _ in range(W+1)]
DP[1][0], DP[0][1] = dist((1,1), A[1]), dist((N,N), A[1])
for i in range(2, W+1):
    DP[i][0] = DP[i-1][0] + dist(A[i-1], A[i])
    DP[0][i] = DP[0][i-1] + dist(A[i-1], A[i])

for a in range(W+1):
    for b in range(W+1):
        if a == b or DP[a][b]: continue

        if abs(a-b) == 1:
            if a - b == 1:
                t = DP[0][b] + dist((1, 1), A[a])
                for c in range(1, b):
                    cur = DP[c][b] + dist(A[c], A[a])
                    if t > cur: t = cur
                DP[a][b] = t
            else:
                t = DP[a][0] + dist((N, N), A[b])
                for c in range(1, a):
                    cur = DP[a][c] + dist(A[c], A[b])
                    if t > cur: t = cur
                DP[a][b] = t
        elif a > b:
            DP[a][b] = DP[a-1][b] + dist(A[a-1], A[a])
        else:
            DP[a][b] = DP[a][b-1] + dist(A[b-1], A[b])

m_a = m_b = 10**6
for i in range(W):
    if m_a > DP[W][i]: m_a = DP[W][i]
    if m_b > DP[i][W]: m_b = DP[i][W]

a_c = b_c = True
ans = [min(m_a, m_b)] + [0] * W
while W > 0:
    m_a = m_b = 10**6
    if a_c:
        for i in range(W):
            if m_a > DP[W][i]:
                m_a = DP[W][i]
                s_a = i
    if b_c:
        for j in range(W):
            if m_b > DP[j][W]:
                m_b = DP[j][W]
                s_b = j

    if m_a > m_b:
        print('#1', W, '||', m_a, m_b, '||', s_a, s_b, '||', ans)
        for i in range(s_b+1, W+1):
            ans[i] = 2
        if s_b: ans[s_b] = 1
        W = s_b
    else:
        print('#2', W, '||', m_a, m_b, '||', s_a, s_b, '||', ans)
        for i in range(s_a+1, W+1):
            ans[i] = 1
        if s_a: ans[s_a] = 2
        W = s_a - 1

print(*ans, sep='\n')
print(*DP, sep='\n')

'''
5
4
5 5
2 3
2 1
1 3
'''