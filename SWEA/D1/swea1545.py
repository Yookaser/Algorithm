# 1545. 거꾸로 출력해 보아요

# 방법1
# N = int(input())

# for i in range(N, -1, -1):
#     print(i, end = ' ')

# 방법2
N = int(input())

for i in reversed(range(0, N + 1)):
    print(i, end = ' ')

# 방법3
N = int(input())

print(*list(range(0, N + 1))[::-1])