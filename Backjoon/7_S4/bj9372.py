# 9372. 상근이의 여행

input = __import__('sys').stdin.readline  # 이게 뭔 표현일까... 처음 봄
ans = []
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M): input()
    ans.append(N-1)  # 뭘 하든 N-1번만에 감

print(*ans, sep='\n')
