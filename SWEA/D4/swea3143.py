# 3143. 가장 빠른 문자열 타이핑

def miniTyping(str1, str2):
    return str1.count(str2) + len(str1.replace(str2, '')) # 포함된 개수 + str1(str2 공백 처리한 길이 반환)


T = int(input())
for test in range(T):
    str1, str2 = map(str, input().split())
    print('#{} {}'.format(test+1, miniTyping(str1, str2)))