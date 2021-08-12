# 콜라츠 추측

def solution(num):
    
    def collatz(num, cnt):
        if cnt >= 500: # 500번이 된 경우
            return -1
        if num == 1: # 답을 찾은 경우
            return cnt
        
        if num % 2 == 0: # 짝수인 경우
            return collatz(num//2, cnt+1)
        else: # 홀수인 경우
            return collatz(num*3+1, cnt+1)
    
    return collatz(num, 0)