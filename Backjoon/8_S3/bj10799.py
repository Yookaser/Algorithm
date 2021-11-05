# 10799. 쇠 막대기

A = list(input())
answer = 0
s = []

for i in range(len(A)):
    if A[i] == '(':
        s.append('(')
    else:
        if A[i-1] == '(': 
            s.pop()
            answer += len(s)
        else:
            s.pop() 
            answer += 1 

print(answer)
