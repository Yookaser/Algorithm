# 42746. 가장 큰 수

def solution(numbers):
    ans = ''.join(sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True))  # 3자리를 맞춰주고 비교하기
    return str(int(ans)) if ans[0] == '0' else ans # [0,0,0] 같은 특수 케이스를 처리하기
