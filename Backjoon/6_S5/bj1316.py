# 1316. 그룹 단어 체커

import sys

input = sys.stdin.readline
N = int(input())
result = 0

for _ in range(N):
    cnt = [0] * 26 # 알파벳 등장 횟수가 들어갈 공간
    alphabets = input().rstrip() # rstrip() 안하면 sys.stdin.readline에서는 빈 공백 하나 들어가서 인덱스 골치 아픔
    print(alphabets, len(alphabets))
    cnt[ord(alphabets[0])-97] += 1 # 첫 번째 인자가 for문에서 안 돌기 때문에 여기서 횟수 기록(아스키 코드 이용 // 소문자만 들어옴)
    
    for i in range(1, len(alphabets)): # 비교를 위해 범위는 1부터 시작
        if alphabets[i-1] != alphabets[i] and cnt[ord(alphabets[i])-97] != 0: # 이전 단어와 같지 않고, cnt 값이 1이 아닐 경우
            break
        cnt[ord(alphabets[i])-97] += 1 # 횟수 기록
    else: # break 안 걸린 경우
        result += 1 # 결과 +1

print(result)