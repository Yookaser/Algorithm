# 42583. 다리를 지나는 트럭

# 방법1. 내 풀이(느림)
from collections import deque


def solution(bridge_length, weight, truck_weights):
    q = deque()  # 다리 위의 트럭을 의미((시간, 무게))
    truck_weights.reverse()  # 대기중인 트럭을 의미
    
    w, t = 0, 0  # 현재 다리의 무게, 시간
    while truck_weights:  # 대기중인 트럭이 없을 때까지
        for i in range(len(q)-1, -1, -1):  # for문 내에서 pop을 해야하므로 뒤에서부터 접근
            if q[i][0] == bridge_length-1:  # 이번에 시간이 증가하면 도착하는 경우
                w -= q[i][1]
                q.pop()  # pop
            else:
                q[i][0] += 1  # 아니면 시간만 +1
        
        x = truck_weights.pop()
        if w + x <= weight:  # 다리 위 트럭 무게 + 진입할 트럭의 무게 <= 허용 무게
            w += x
            q.appendleft([0, x])  # [시간, 무게]를 의미(위에서 값 변경하므로 튜플 안됨 // 앞으로 추가함)
        else:
            truck_weights.append(x)  # 아닌 경우는 다시 재자리
        t += 1  # 시간 증가
    t += bridge_length  # 마지막 트럭이 다리 위에 올라간 것이므로 다리 길이만큼 +

    return t

# 방법2. 다른 사람 풀이(빠름)
# from collections import deque


# def solution(bridge_length, weight, truck_weights):
#     q = deque(0 for _ in range(bridge_length))  # 다리를 구현(각 숫자는 무게 초기는 0)
#     truck_weights.reverse()  # 대기중인 트럭을 의미
    
#     w, t = 0, 0  # 현재 다리의 무게, 시간
#     while truck_weights:
#         w -= q.popleft()  # 
#         if w + truck_weights[-1] <= weight:  # 다리에 진입 가능한 경우
#             w += truck_weights[-1]
#             q.append(truck_weights.pop())
#         else:  # 다리 진입이 불가능한 경우
#             q.append(0)  # 무게 0을 추가
#         t += 1
#     t += bridge_length  # 마지막 트럭이 다리 위에 올라간 것이므로 다리 길이만큼 +

#     return t
