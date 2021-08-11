# 이진 변환 반복하기

def solution(s):
    bin_cnt = 0 # 2진 변환 카운팅
    zero_cnt = 0 # 0 제거 카운팅
    
    while s != '1':
        if '0' in s: # 0이 있다면
            result = 0 # 0 숫자 카운팅
            for i in s:
                if i == '0':
                    result += 1
            s = '1' * (len(s) - result) # 1의 개수를 구해서 다시 만듬
            zero_cnt += result

        s = format(len(s), 'b') # 2진 변환(어차피 길이 -> 2진 변환해야하므로 종료 조건을 걸 필요 없음)
        bin_cnt += 1
        
    return [bin_cnt, zero_cnt]