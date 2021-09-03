# 42586. 기능 개발

def solution(progresses, speeds):
    ans, temp = [], []
    
    for i in range(len(progresses)):  # 작업 일수 계산
        x = 100 - progresses[i]
        
        if (x//speeds[i]) == (x/speeds[i]):  # 나누어 떨어지는 경우
            temp.append(x // speeds[i])
        else:  # 나누어 떨어지지 않는 경우
            temp.append((x//speeds[i]) + 1)
    
    idx = 0  # 현재의 idx 기록
    for i in range(len(temp)):  # 배포 계산(progresses가 없는 경우 실행 안됨)
        if not ans:  # 값이 없는 경우(처음에만 실행됨)
            ans.append(1)
        else:
            if temp[i] <= temp[idx]:  # 작업 일수가 더 작은 경우
                ans[-1] += 1
            else:  # 더 큰 경우
                ans.append(1)  # 새로 1을 추가
                idx = i
    
    return ans
