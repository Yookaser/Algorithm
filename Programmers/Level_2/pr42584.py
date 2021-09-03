# 42584. 주식 가격

# 방법1. 내 풀이(느림)
def solution(prices):
    l = len(prices)
    ans = [0] * l
    c = [0] * 10001  # 인덱스 숫자의 값보다 작은 인덱스를 저장
        
    for i in range(l):
        x = prices[i]
        
        if i >= c[x]:  # 해당 인덱스보다 작은 인덱스 번호 보다 내 인덱스 번호가 큰 경우
            for j in range(i+1, l):  # 더 작은 값 찾기
                if x > prices[j]:
                    c[x] = j
                    ans[i] = j - i
                    break
            else:  # 만약 못 찾았으면 길이를 이용
                c[x] = l - 1
                ans[i] = c[x] - i
        else:  # 나와 같은 값의 인덱스에 값이 나의 인덱스보다 작은 경우
            ans[i] = c[prices[i]] - i
    return ans

# 방법2. 다른 사람 풀이(빠름)
# def solution(prices):
#     stack = []
#     answer = [0] * len(prices)

#     for i in range(len(prices)):
#         if stack != []:
#             while stack != [] and stack[-1][1] > prices[i]:  # 스택이 있고 스택 마지막 값보다 배열의 값이 작은 경우 반복
#                 past, _ = stack.pop()
#                 answer[past] = i - past
#         stack.append([i, prices[i]])  # 현재 값 push

#     for i, s in stack:
#         answer[i] = len(prices) - 1 - i
#     return answer