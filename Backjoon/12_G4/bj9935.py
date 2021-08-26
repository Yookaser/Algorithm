# 9935. 문자열 폭발

words = input()
pattern = list(input())  # 비교를 위해 리스트로 입력 받아줌
stack = []  # 단어를 쌓을 공간
length, last = len(pattern), pattern[-1]  # pattern의 길이와 마지막 글자를 저장

for w in words:
    stack.append(w)
    if w == last and stack[-length:] == pattern:  # 마지막 글자가 스택의 마지막과 동일하고 패턴 길이만큼 뽑은 리스트가 패턴(리스트)와 동일한 경우
        del stack[-length:]  # 해당 길이만큼 제거

if stack:  # 스택 안 빈 경우
    print(''.join(stack))
else:  # 빈 경우
    print('FRULA')