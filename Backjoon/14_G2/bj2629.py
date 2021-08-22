# 2629 양팔저울

def scale(now, left, right, possible):
    new = abs(left-right)
    if new not in possible: possible.append(new)
    if now == n: return 0
    if answer[now][new] == 0:
        scale(now+1, left+n_list[now], right, possible)
        scale(now+1, left, right+n_list[now], possible)
        scale(now+1, left, right, possible)
        
        answer[now][new] = 1

n = int(input(""))
n_list = list(map(int, input().split()))
m = int(input(""))
m_list = list(map(int, input().split()))
possible = []
answer = [[0]*15001 for i in range(n+1)]


scale(0, 0, 0, possible)
for i in range(0,len(m_list)):
    if(m_list[i] in possible):
        print("Y",end=' ')
    else:
        print("N",end=' ')