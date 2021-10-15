# 87389. 나머지가 1이 되는 수 찾기

def solution(n):
    for i in range(1, n):
        if n % i == 1:
            break
    return i
