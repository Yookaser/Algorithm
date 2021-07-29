# 1976. 시각 덧셈

def time_add(H1, M1, H2, M2):
    H_sum = H1 + H2
    M_sum = M1 + M2

    if H_sum >= 13: # 12시를 넘어갈 경우
        H_sum -= 12

    if M_sum >= 60: # 60분을 넘어갈 경우
        M_sum %= 60
        H_sum += 1
    
    return H_sum, M_sum

T = int(input())

for _ in range(T):
    h1, m1, h2, m2 = list(map(int, input().split()))
    h, m = time_add(h1, m1, h2, m2)
    print(f'#{_ + 1} {h} {m}')