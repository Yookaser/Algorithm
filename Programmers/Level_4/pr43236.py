# 43236. 징검다리

def solution(distance, rocks, n):
    rocks.sort()  # 정렬이 필요
    l, r = 1, distance  # l = 가장 작은 값, r = 가장 큰 값
    
    while l <= r:  # 이분 탐색
        m = (l+r) // 2  # 현재 바위의 거리
        c, s = 0, 0  # c: 현재 바위 위치, s: 제거한 바위의 수
        
        for r in rocks:  # 바위 반복
            if r - c < m: s += 1  # 만약 바위의 거리의 차가 m보다 작은 경우 제거 +1
            else: c = r  # m보다 크다면 현재 바위 위치를 갱신
                
            if s > n:    # 시간 단축을 위해 n보다 커지면 정지
                break
        
        if s > n:  # 절단 바위의 수가 더 많은 경우(최대 거리 줄이기)
            r = m - 1
        else:  # 절단 바위의 수가 더 적은 경우(최소 거리 늘리기)
            l = m + 1
            
    return l - 1  # 최소 거리에서 -1 반환