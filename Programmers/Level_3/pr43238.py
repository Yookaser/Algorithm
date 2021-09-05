# 43238. 입국 심사

def solution(n, times):
    l, r = 1, max(times) * n  # l = 가장 작은 값, r = 가장 큰 값
    
    while l < r:  # 이분 탐색
        m = (l+r) // 2
        s = 0  # 배정 받은 사람의 수
        
        for t in times:  # 시간 반복
            s += m // t  # 
        
        if s >= n:  # 배정 받은 사람이 더 많거나 같은 경우
            r = m  # 최대 시간을 시간을 줄여보기
        else:  # 배정 받은 사람이 더 적은 경우
            l = m + 1  # 최소 시간을 늘려보기
    
    return l  # 최소 시간을 반환
