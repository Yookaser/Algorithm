# 42748. K번째수

def solution(array, commands):
    ans = []
    
    for command in commands:
        i, j, k = command
        ans.append(sorted(array[i-1:j])[k-1])  # 정렬 후 인덱스에 접근(sorted는 정렬 리스트 반환)
    
    return ans
