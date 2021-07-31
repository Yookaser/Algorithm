# 6064. 카잉 달력

def kaing(M, N, x, y): # 이 문제는 (1,1) -> (x,y)를 만드는 문제
    while x <= M*N: 
        if x % N == y % N: # 처음에는 x % N == y라고 생각했지만, 이러면 x % N은 0이 나오는데 y는 N인 경우 등이 생김
            return x # 답을 찾은 경우(만들어야 하는 x에서 M을 계속 더한 값이 횟수가 됨)
        x += M
    return -1 # 못 찾은 경우

T = int(input())

for i in range(T):
    M, N, x, y = map(int, input().split())
    print(kaing(M, N, x, y))