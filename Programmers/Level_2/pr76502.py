# 76502. 괄호 회전하기

def solution(s):
    answer = 0
    pair = {')': '(', '}': '{', ']': '['} # 짝 지어 놓기
    s_list = list(s)
    
    for i in range(len(s)):
        s_list.append(s_list.pop(0)) # 한 칸씩 움직이기
        stack = []
        for i in s_list:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                if len(stack) == 0 or pair[i] != stack.pop(): # pop을 할 수 없고, 나온 값이 pair가 아닌 경우
                    break
        else: # for문이 정상적을 실행된 경우
            if len(stack) == 0: # stack이 0인 경우(남아 있으면 올바른 괄호 문자열이 아님)
                answer += 1
    return answer