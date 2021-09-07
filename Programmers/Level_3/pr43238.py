# 43238. 입국 심사

def solution(n, times):
    l, r = 1, max(times) * n  # l = 가장 작은 값, r = 가장 큰 값
    
    while l <= r:  # 이분 탐색
        m = (l+r) // 2
        s = 0  # 배정 받은 사람의 수
        
        for t in times:  # 시간 반복
            s += m // t  # 입국 심사 시간으로 나눈 몫만큼 배정 받은 사람 수 추가
            if s >= n:  # 시간 단축을 위해 n보다 크거나 같아지면 정지
                break
        
        if s >= n:  # 배정 받은 사람이 더 많거나 같은 경우(최대 시간 줄이기)
            r = m - 1
        else:  # 배정 받은 사람이 더 적은 경우(최소 시간 늘리기)
            l = m + 1
    
    return l  # 최소 시간을 반환
