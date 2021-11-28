# 1406. 에디터

from sys import stdin


input = stdin.readline
A = list(input()[:-1])
N = int(input())
ans = []

for _ in range(N):
    cmd = input()
    if cmd[0] == 'L' and A:
        ans.append(A.pop())
    elif cmd[0] == 'D' and ans:
        A.append(ans.pop())
    elif cmd[0] == 'B' and A:
        A.pop()
    elif cmd[0] == 'P':
        A.append(cmd[2])

print(''.join(A + ans[::-1]))
