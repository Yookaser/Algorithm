# 1918. 후위 표기식

def postOrder(notation):
    global result # 재귀를 사용해서 global이 필요함
    stack = [] # 연산자를 저장할 공간

    while notation:
        if notation[0].isalpha(): # 알파뱃인 경우
            result += notation.popleft() # 단순히 결과에 더해줌
        elif notation[0] == '(': # 괄호가 열린 경우
            notation.popleft() # 해당 괄호 제거
            postOrder(notation) # 재귀
        elif notation[0] == ')': # 괄호가 닫힌 경우
            notation.popleft() # 괄호 제거
            break # while 문 벗어나게 만들고 stack에 남은 것 result에 다 더해줘서 재귀 끝나게 함(')'가 나온 경우는 재귀로 들어간 경우만 있음)
        elif notation[0] in ('*', '/'): # 곱셈, 나눗셈인 경우('+', '-'보다 연산 우선이므로 분리해서 조건 취급)
            if stack: # stack이 비어있지 않은 경우
                value = stack.pop()
                if value not in ('+', '-'): # stack의 마지막 값이 곱셈, 나눗셈인 경우(pop으로 뱉은 값 결과에 저장하고, 현재값 stack에 쌓아줌)
                    result += value
                    stack.append(notation.popleft())
                else: # stack의 마지막 값이 덧셈, 뺄셈인 경우(추가적인 연산?계산 못함 그냥 스택에 쌓아줌)
                    stack.append(value)
                    stack.append(notation.popleft())
            else: # 비어있는 경우(그냥 stack에 쌓음)
                 stack.append(notation.popleft())
        else: # 덧셈, 뺄셈인 경우
            if stack: # stack이 비어있지 않은 경우(연산 우선순위 낮으므로 pop으로 다 꺼내서 result에 더해줌 -> **이거 매우 중요함**)
                result += stack.pop()
            else: # 비어있는 경우(그냥 stack에 쌓음)
                stack.append(notation.popleft())
    
    if stack: # while문이 끝나도 stack이 쌓여 있는 경우(EX -> +, - 이후 *, /이 온 경우)
        while stack:
            result += stack.pop()

from collections import deque

notation = deque(input())
result = '' # 결과를 저장할 공간
postOrder(notation)
print(result)