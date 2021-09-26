# 42862. 체육복

def solution(n, lost, reserve):
    lost, reserve = set(lost) - set(reserve), set(reserve) - set(lost)  # 교집합 제거한 집합 생성
    
    ans = n - len(lost)
    for i in lost:
        if (i-1) in reserve:
            ans += 1
            reserve.remove(i-1)  # 빌려줬으므로 제거
        elif (i+1) in reserve:
            ans += 1
            reserve.remove(i+1)
    
    return ans
