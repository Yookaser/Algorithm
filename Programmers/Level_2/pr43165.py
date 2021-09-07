# 43165. 타겟 넘버

def solution(numbers, target):
    ans = 0 
    
    def make(i, c):
        nonlocal ans
        if i == len(numbers): # base case
            if c == target:  # 같으면 ans +1
                ans += 1
            return
        
        make(i+1, c+numbers[i])  # +
        make(i+1, c-numbers[i])  # -
    
    make(0, 0)  # 시작 인덱스 0, 시작 값 0
    return ans
    