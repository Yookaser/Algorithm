# 70130. 스타 수열

def solution(arr):
    length = len(arr)
    counting = [[0, None] for _ in range(length+1)] # 카운팅할 2차원 리스트(인덱스: arr 요소의 숫자, [0, None]: 0 자리는 카운팅/None 자리는 어느 인덱스와 연결해서 카운팅했는지)
    confirm = [False] * (length+1) # 카운팅 했는지 체크할 리스트(인덱스: arr의 인덱스, Fasle: 카운팅 안함)

    for i in range(1, length): # 0은 인덱스상 돌면 안됨(1부터!)
        if arr[i-1] != arr[i]: # 다른 경우
            if counting[arr[i-1]][1] != i and not confirm[i-1]: # arr[i-1]의 값과 같은 숫자가 같은 인덱스와 연결해서 카운팅하지 않고, i-1번째 인덱스가 카운팅 안된 경우
                counting[arr[i-1]][0] += 1 # 카운팅 +1
                counting[arr[i-1]][1] = i # 연결 인덱스 변경
                confirm[i-1] = True # 카운팅 한 것으로 변경
            if counting[arr[i]][1] != i-1 and not confirm[i]: # 위의 i-1 작업과 같음
                counting[arr[i]][0] += 1
                counting[arr[i]][1] = i-1
                confirm[i] = True

    return max(counting)[0]*2 # 2차원 리스트이므로 튜플 형태로 max 출력됨(0번째 인덱스가 카운팅이므로 이 값의 2배를 반환해줌)