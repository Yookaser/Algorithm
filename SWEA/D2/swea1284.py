# 1284. 수도 요금 경쟁

def water_cost(P, Q, R, S, W):
    A_cost = W * P
    
    if W > R: # R을 넘을 때
        B_cost = Q + (W - R) * S
    else: # R을 안넘을 때
        B_cost = Q

    return A_cost if A_cost <= B_cost else B_cost 

T = int(input())

for _ in range(T):
    P, Q, R, S, W = list(map(int, input().split()))
    
    print(f'#{_ + 1} {water_cost(P, Q, R, S, W)}')