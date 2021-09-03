# 42587. 프린터

# 방법1. 내 풀이(복잡함)
from collections import deque


def solution(priorities, location):
    ans = []
    x, l = priorities[location], len(priorities)  # 해당 값, 길이
    priorities = deque(priorities)
    
    while True:
        if location == 0:  # 목적 값이 제일 앞인 경우
            for i in range(1, l):
                if priorities[i] > x:  # 더 큰 값이 있는 경우
                    location = l - 1
                    priorities.append(priorities.popleft())  # 맨 앞을 맨 뒤로
                    break
            else:  # 목적 값이 제일 앞에 있는 경우
                ans.append(x)
                break
        else:  # 목적 값이 제일 앞이 아닌 경우
            for i in range(1, l):  # 뒤에 더 큰 값이 있는지 반복
                if priorities[i] > priorities[0]:
                    location -= 1
                    priorities.append(priorities.popleft())
                    break
            else:  # 제일 큰 값이 앞에 온 경우
                ans.append(priorities.popleft())
                location -= 1  # 목적 값 위치 -1
                l -= 1  # 전체 길이 -1

    return len(ans)

# 방법2. 다른 사람 풀이(간단함)
# from collections import deque


# def solution(priorities, location):
#     queue =  deque((i,p) for i,p in enumerate(priorities))  # 인덱스, 우선순위
#     answer = 0
#     while True:
#         cur = queue.popleft(0)
#         if any(cur[1] < q[1] for q in queue):  # 하나라도 더 큰 숫자가 있으면 True 반환됨
#             queue.append(cur)
#         else:  # 맨 앞이 제일 큰 숫자인 경우
#             answer += 1  # +1
#             if cur[0] == location:
#                 return answer
