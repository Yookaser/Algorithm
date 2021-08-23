# 10942. 팰린드롬?

# 방법1.

def palindrome(S, E):
    if DP[S][E] == -1:  # 값을 구한 적이 없는 경우
        for i in range((E-S)//2+1):  # 팰린드롬인지 확인
            if arr[S+i] != arr[E-i]:
                DP[S][E] = 0
                break
        else: DP[S][E] = 1
    return DP[S][E]  # 값 반환


import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
DP = [[-1] * N for _ in range(N)]

for i in range(int(input())):
    start, end = map(int, input().split())
    print(palindrome(start-1, end-1))  # 인덱스를 맞추기 위해 -1

# 방법2. 

# from sys import stdin

# input = stdin.readline
# N = int(input())
# arr = list(map(int, input().split()))
# DP = [[0] * N for _ in range(N)]

# for i in range(N-1):  # 자기 자신과 자기자신 바로 다음이 팰린드롬인지 입력
#     DP[i][i] = 1  # 자기자신은 무조건 팰린드롬
#     DP[i][i+1] += (arr[i]==arr[i+1])  # 자기자신과 다음칸이 같다면 +1
# DP[N-1][N-1] = 1  # 인덱스 에러를 피하기 위해 해당 칸은 직접 입력

# for g in range(2, N):  # DP에서 대각선 기준 우상단만 도는 것(어차피 E는 S보다 무조건 크거나 같기 때문)
#     for i in range(N-g):
#         j = i + g  # j(열)은 해당 i보다 2이상 큰 값이 들어가야 함(자기자신 뒤의 1칸은 위에서 이미 함)
#         DP[i][j] = DP[i+1][j-1] * (arr[i]==arr[j])

# for i in range(int(input())):
#     start, end = map(int, input().split())
#     print(DP[start-1][end-1])