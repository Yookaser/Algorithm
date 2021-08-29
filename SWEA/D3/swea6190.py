# 6190. 정곤이의 단조 증가하는 수

def check(x):
    nx = x % 10
    x //= 10
    while x:  # x 가 0이 아닐때까지
        sx = x % 10
        if sx > nx:  # 단조 증가가 아닌 경우
            return False
        nx = sx
        x //= 10
    return True


T = int(input())
for test in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())), reverse=True)
    visited = set()
    ans = -1  # 답이 없는 경우 -1 출력해야 하므로 -1

    for i in range(N):
        for j in range(i+1, N):
            num = arr[i] * arr[j]
            if num > ans and num not in visited and check(num):  # 해당 수가 더 크고, 나온 적이 없고, 단조 증가인 경우
                ans = max(ans, num)  # 더 큰 값을 넣어줌
                visited.add(num)

    print('#{} {}'.format(test+1, ans))
